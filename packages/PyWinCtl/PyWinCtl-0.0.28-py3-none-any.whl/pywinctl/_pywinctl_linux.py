#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import platform
import subprocess
import sys
import time
from typing import Union, List

import Xlib.X
import Xlib.display
import Xlib.protocol
from Xlib.xobject.colormap import Colormap
from Xlib.xobject.cursor import Cursor
from Xlib.xobject.drawable import Drawable, Pixmap, Window
from Xlib.xobject.fontable import Fontable, GC, Font
from Xlib.xobject.resource import Resource
import ewmh
from pynput import mouse

from pywinctl import pointInRect, BaseWindow, Rect, Point, Size

DISP = Xlib.display.Display()
SCREEN = DISP.screen()
ROOT = DISP.screen().root
EWMH = ewmh.EWMH(_display=DISP, root=ROOT)

# WARNING: Changes are not immediately applied, specially for hide/show (unmap/map)
#          You may set wait to True in case you need to effectively know if/when change has been applied.
WAIT_ATTEMPTS = 10
WAIT_DELAY = 0.025  # Will be progressively increased on every retry

# These _NET_WM_STATE_ constants are used to manage Window state and are documented at
# https://ewmh.readthedocs.io/en/latest/ewmh.html
WM_CHANGE_STATE = 'WM_CHANGE_STATE'
WM_STATE = '_NET_WM_STATE'
STATE_MODAL = '_NET_WM_STATE_MODAL'
STATE_STICKY = '_NET_WM_STATE_STICKY'
STATE_MAX_VERT = '_NET_WM_STATE_MAXIMIZED_VERT'
STATE_MAX_HORZ = '_NET_WM_STATE_MAXIMIZED_HORZ'
STATE_SHADED = '_NET_WM_STATE_SHADED'
STATE_SKIP_TASKBAR = '_NET_WM_STATE_SKIP_TASKBAR'
STATE_SKIP_PAGER = '_NET_WM_STATE_SKIP_PAGER'
STATE_HIDDEN = '_NET_WM_STATE_HIDDEN'
STATE_FULLSCREEN = '_NET_WM_STATE_FULLSCREEN'
STATE_ABOVE = '_NET_WM_STATE_ABOVE'
STATE_BELOW = '_NET_WM_STATE_BELOW'
STATE_ATTENTION = '_NET_WM_STATE_DEMANDS_ATTENTION'
STATE_FOCUSED = '_NET_WM_STATE_FOCUSED'
STATE_NULL = 0

# EWMH/Xlib set state actions
ACTION_UNSET = 0   # Remove state
ACTION_SET = 1     # Add state
ACTION_TOGGLE = 2  # Toggle state

# EWMH/Xlib WINDOW_TYPE values
WM_WINDOW_TYPE = '_NET_WM_WINDOW_TYPE'
WINDOW_DESKTOP = '_NET_WM_WINDOW_TYPE_DESKTOP'
WINDOW_NORMAL = '_NET_WM_WINDOW_TYPE_NORMAL'

# EWMH/Xlib State Hints
HINT_STATE_WITHDRAWN = 0
HINT_STATE_NORMAL = 1
HINT_STATE_ICONIC = 3


def getActiveWindow():
    """
    Get the currently active (focused) Window

    :return: Window object or None
    """
    win_id = EWMH.getActiveWindow()
    if win_id:
        return LinuxWindow(win_id)
    return None


def getActiveWindowTitle() -> str:
    """
    Get the title of the currently active (focused) Window

    :return: window title as string or empty
    """
    win = getActiveWindow()
    if win:
        return win.title
    else:
        return ""


def getWindowsAt(x: int, y: int):
    """
    Get the list of Window objects whose windows contain the point ``(x, y)`` on screen

    :param x: X screen coordinate of the window(s)
    :param y: Y screen coordinate of the window(s)
    :return: list of Window objects
    """
    windowsAtXY = []
    for win in getAllWindows():
        if pointInRect(x, y, win.left, win.top, win.width, win.height):
            windowsAtXY.append(win)
    return windowsAtXY


def getWindowsWithTitle(title: str):
    """
    Get the list of Window objects whose title match the given string

    :param title: title of the desired windows as string
    :return: list of Window objects
    """
    matches = []
    for win in getAllWindows():
        if win.title == title:
            matches.append(win)

    return matches


def getAllTitles() -> List[str]:
    """
    Get the list of titles of all visible windows

    :return: list of titles as strings
    """
    return [window.title for window in getAllWindows()]


def getAllWindows():
    """
    Get the list of Window objects for all visible windows

    :return: list of Window objects
    """
    windows = EWMH.getClientList()
    return [LinuxWindow(window) for window in windows]


def _xlibGetAllWindows(parent: int = None, title: str = "") -> List[int]:
    # Not using window class (get_wm_class())

    if not parent:
        parent = ROOT
    allWindows = [parent]

    def findit(hwnd):
        query = hwnd.query_tree()
        for child in query.children:
            allWindows.append(child)
            findit(child)

    findit(parent)
    if not title:
        matches = allWindows
    else:
        matches = []
        for w in allWindows:
            if w.get_wm_name() == title:
                matches.append(w)
    return matches


def getAllAppsTitles() -> List[str]:
    """
    Get the list of names of all visible apps

    :return: list of names as strings
    """
    return list(getAllAppsWindowsTitles().keys())


def getAllAppsWindowsTitles() -> dict:
    """
    Get all visible apps names and their open windows titles

    Format:
        Key: app name

        Values: list of window titles as strings

    :return: python dictionary
    """
    result = {}
    for win in getAllWindows():
        appName = win.getAppName()
        if appName in result.keys():
            result[appName].append(win.title)
        else:
            result[appName] = [win.title]
    return result


class LinuxWindow(BaseWindow):

    def __init__(self, hWnd: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]):
        super().__init__()
        self._hWnd = hWnd
        self._parent = self._hWnd.query_tree().parent
        self._setupRectProperties()
        # self._saveWindowInitValues()  # Store initial Window parameters to allow reset and other actions

    def _getWindowRect(self) -> Rect:
        # https://stackoverflow.com/questions/12775136/get-window-position-and-size-in-python-with-xlib - mgalgs
        win = self._hWnd
        geom = win.get_geometry()
        x = geom.x
        y = geom.y
        while True:
            parent = win.query_tree().parent
            pgeom = parent.get_geometry()
            x += pgeom.x
            y += pgeom.y
            if parent.id == ROOT.id:
                break
            win = parent
        w = geom.width
        h = geom.height

        return Rect(x, y, x + w, y + h)

    def _saveWindowInitValues(self) -> None:
        # Saves initial rect values to allow reset to original position, size, state and hints.
        self._init_left, self._init_top, self._init_right, self._init_bottom = self._getWindowRect()
        self._init_width = self._init_right - self._init_left
        self._init_height = self._init_bottom - self._init_top
        self._init_state = self._hWnd.get_wm_state()
        self._init_hints = self._hWnd.get_wm_hints()
        self._init_normal_hints = self._hWnd.get_wm_normal_hints()
        # self._init_attributes = self._hWnd.get_attributes()  # can't be modified, so not saving it

    def __repr__(self):
        return '%s(hWnd=%s)' % (self.__class__.__name__, self._hWnd)

    def __eq__(self, other):
        return isinstance(other, LinuxWindow) and self._hWnd == other._hWnd

    def close(self) -> bool:
        """
        Closes this window. This may trigger "Are you sure you want to
        quit?" dialogs or other actions that prevent the window from
        actually closing. This is identical to clicking the X button on the
        window.

        :return: ''True'' if window is closed
        """
        EWMH.setCloseWindow(self._hWnd)
        EWMH.display.flush()
        return self._hWnd not in EWMH.getClientList()

    def minimize(self, wait: bool = False) -> bool:
        """
        Minimizes this window

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window minimized
        """
        if not self.isMinimized:
            prop = DISP.intern_atom(WM_CHANGE_STATE, False)
            data = (32, [Xlib.Xutil.IconicState, 0, 0, 0, 0])
            ev = Xlib.protocol.event.ClientMessage(window=self._hWnd.id, client_type=prop, data=data)
            mask = Xlib.X.SubstructureRedirectMask | Xlib.X.SubstructureNotifyMask
            ROOT.send_event(event=ev, event_mask=mask)
            # These other options are equivalent to previous code. Keeping them as a mere reference
            # DISP.send_event(destination=ROOT, event=ev, event_mask=mask)
            # data = [Xlib.Xutil.IconicState, 0, 0, 0, 0]
            # EWMH._setProperty(_type="WM_CHANGE_STATE", data=data, mask=mask)
            DISP.flush()
            retries = 0
            while wait and retries < WAIT_ATTEMPTS and not self.isMinimized:
                retries += 1
                time.sleep(WAIT_DELAY * retries)
        return self.isMinimized

    def maximize(self, wait: bool = False) -> bool:
        """
        Maximizes this window

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window maximized
        """
        if not self.isMaximized:
            EWMH.setWmState(self._hWnd, ACTION_SET, STATE_MAX_VERT, STATE_MAX_HORZ)
            EWMH.display.flush()
            retries = 0
            while wait and retries < WAIT_ATTEMPTS and not self.isMaximized:
                retries += 1
                time.sleep(WAIT_DELAY * retries)
        return self.isMaximized

    def restore(self, wait: bool = False) -> bool:
        """
        If maximized or minimized, restores the window to it's normal size

        :param wait: set to ''True'' to confirm action requested (in a reasonable time)
        :return: ''True'' if window restored
        """
        self.activate(wait=wait)
        if self.isMaximized:
            EWMH.setWmState(self._hWnd, ACTION_UNSET, STATE_MAX_VERT, STATE_MAX_HORZ)
            EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.isMaximized or self.isMinimized):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return not self.isMaximized and not self.isMinimized

    def show(self, wait: bool = False) -> bool:
        """
        If hidden or showing, shows the window on screen and in title bar

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window showed
        """
        win = DISP.create_resource_object('window', self._hWnd)
        win.map()
        DISP.flush()
        win.map_sub_windows()
        DISP.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and not self._isMapped:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self._isMapped

    def hide(self, wait: bool = False) -> bool:
        """
        If hidden or showing, hides the window from screen and title bar

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window hidden
        """
        win = DISP.create_resource_object('window', self._hWnd)
        win.unmap_sub_windows()
        DISP.flush()
        win.unmap()
        DISP.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and self._isMapped:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return not self._isMapped

    def activate(self, wait: bool = False) -> bool:
        """
        Activate this window and make it the foreground (focused) window

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window activated
        """
        if "arm" in platform.platform():
            EWMH.setWmState(self._hWnd, ACTION_UNSET, STATE_BELOW, STATE_NULL)
            EWMH.display.flush()
            EWMH.setWmState(self._hWnd, ACTION_SET, STATE_ABOVE, STATE_FOCUSED)
        else:
            EWMH.setActiveWindow(self._hWnd)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and not self.isActive:
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.isActive

    def resize(self, widthOffset: int, heightOffset: int, wait: bool = False) -> bool:
        """
        Resizes the window relative to its current size

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window resized to the given size
        """
        return self.resizeTo(self.width + widthOffset, self.height + heightOffset, wait)

    resizeRel = resize  # resizeRel is an alias for the resize() method.

    def resizeTo(self, newWidth: int, newHeight: int, wait: bool = False) -> bool:
        """
        Resizes the window to a new width and height

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window resized to the given size
        """
        EWMH.setMoveResizeWindow(self._hWnd, x=self.left, y=self.top, w=newWidth, h=newHeight)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.width != newWidth or self.height != newHeight):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.width == newWidth and self.height == newHeight

    def move(self, xOffset: int, yOffset: int, wait: bool = False) -> bool:
        """
        Moves the window relative to its current position

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window moved to the given position
        """
        newLeft = max(0, self.left + xOffset)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, self.top + yOffset)
        return self.moveTo(newLeft, newTop, wait)

    moveRel = move  # moveRel is an alias for the move() method.

    def moveTo(self, newLeft:int, newTop: int, wait: bool = False) -> bool:
        """
        Moves the window to new coordinates on the screen

        :param wait: set to ''True'' to wait until action is confirmed (in a reasonable time lap)
        :return: ''True'' if window moved to the given position
        """
        newLeft = max(0, newLeft)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, newTop)
        EWMH.setMoveResizeWindow(self._hWnd, x=newLeft, y=newTop, w=self.width, h=self.height)
        EWMH.display.flush()
        retries = 0
        while wait and retries < WAIT_ATTEMPTS and (self.left != newLeft or self.top != newTop):
            retries += 1
            time.sleep(WAIT_DELAY * retries)
        return self.left == newLeft and self.top == newTop

    def _moveResizeTo(self, newLeft: int, newTop: int, newWidth: int, newHeight: int) -> bool:
        newLeft = max(0, newLeft)  # Xlib/EWMH won't accept negative positions
        newTop = max(0, newTop)
        EWMH.setMoveResizeWindow(self._hWnd, x=newLeft, y=newTop, w=newWidth, h=newHeight)
        EWMH.display.flush()
        return newLeft == self.left and newTop == self.top and newWidth == self.width and newHeight == self.height

    def alwaysOnTop(self, aot: bool = True) -> bool:
        """
        Keeps window on top of all others.

        :param aot: set to ''False'' to deactivate always-on-top behavior
        :return: ''True'' if command succeeded
        """
        action = ACTION_SET if aot else ACTION_UNSET
        EWMH.setWmState(self._hWnd, action, STATE_ABOVE)
        EWMH.display.flush()
        return STATE_ABOVE in EWMH.getWmState(self._hWnd, str=True)

    def alwaysOnBottom(self, aob: bool = True) -> bool:
        """
        Keeps window below of all others, but on top of desktop icons and keeping all window properties

        :param aob: set to ''False'' to deactivate always-on-bottom behavior
        :return: ''True'' if command succeeded
        """
        action = ACTION_SET if aob else ACTION_UNSET
        EWMH.setWmState(self._hWnd, action, STATE_BELOW)
        EWMH.display.flush()
        return STATE_BELOW in EWMH.getWmState(self._hWnd, str=True)

    def lowerWindow(self) -> bool:
        """
        Lowers the window to the bottom so that it does not obscure any sibling windows

        :return: ''True'' if window lowered
        """
        w = DISP.create_resource_object('window', self._hWnd)
        w.configure(stack_mode=Xlib.X.Below)
        DISP.flush()
        windows = EWMH.getClientListStacking()
        return windows and self._hWnd == windows[-1]

    def raiseWindow(self) -> bool:
        """
        Raises the window to top so that it is not obscured by any sibling windows.

        :return: ''True'' if window raised
        """
        w = DISP.create_resource_object('window', self._hWnd)
        w.configure(stack_mode=Xlib.X.Above)
        DISP.flush()
        windows = EWMH.getClientListStacking()
        return windows and self._hWnd == windows[0]

    def sendBehind(self, sb: bool = True) -> bool:
        """
        Sends the window to the very bottom, below all other windows, including desktop icons.
        It may also cause that the window does not accept focus nor keyboard/mouse events as well as
        make the window disappear from taskbar and/or pager.

        :param sb: set to ''False'' to bring the window back to front
        :return: ''True'' if window sent behind desktop icons

        Notes:
            - On GNOME it will obscure desktop icons... by the moment
        """
        if sb:
            # https://stackoverflow.com/questions/58885803/can-i-use-net-wm-window-type-dock-ewhm-extension-in-openbox
            w = DISP.create_resource_object('window', self._hWnd)
            # Place a Window behind desktop icons using PyQt on Ubuntu/GNOME
            # This adds the properties (notice the PropMode options), but with no effect on GNOME
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_BELOW, False), ],
                              Xlib.X.PropModeReplace)
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_SKIP_TASKBAR, False), ],
                              Xlib.X.PropModeAppend)
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_SKIP_PAGER, False), ],
                              Xlib.X.PropModeAppend)
            DISP.flush()

            # This sends window below all others, but not behind the desktop icons
            w.change_property(DISP.intern_atom(WM_WINDOW_TYPE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(WINDOW_DESKTOP, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()

            if "GNOME" in os.environ.get('XDG_CURRENT_DESKTOP', ''):
                pass
                # This sends the window "too far behind" (below all others, including Wallpaper, like unmapped)
                # Trying to figure out how to raise it on top of wallpaper but behind desktop icons
                # TODO: As an idea, find Wallpaper window to try to reparent our window to it, or to its same parent
                # desktop = _xlibGetAllWindows(title="gnome-shell")  # or "main", not sure...
                # if desktop:
                #     w.reparent(desktop[-1], self.left, self.top)
                #     DISP.flush()

            else:
                # Mint/Cinnamon: just clicking on the desktop, it raises, sending the window/wallpaper to the bottom!
                # TODO: Find a smarter way to raise desktop icons instead of a mouse click
                m = mouse.Controller()
                m.move(SCREEN.width_in_pixels - 1, 100)
                m.click(mouse.Button.left, 1)
            return WINDOW_DESKTOP in EWMH.getWmWindowType(self._hWnd, str=True)
        else:
            w = DISP.create_resource_object('window', self._hWnd)
            w.unmap()
            w.change_property(DISP.intern_atom(WM_WINDOW_TYPE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(WINDOW_NORMAL, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()
            w.change_property(DISP.intern_atom(WM_STATE, False), Xlib.Xatom.ATOM,
                              32, [DISP.intern_atom(STATE_FOCUSED, False), ],
                              Xlib.X.PropModeReplace)
            DISP.flush()
            w.map()
            EWMH.setActiveWindow(self._hWnd)
            EWMH.display.flush()
            return WINDOW_NORMAL in EWMH.getWmWindowType(self._hWnd, str=True) and self.isActive

    def getAppName(self) -> str:
        """
        Get the name of the app current window belongs to

        :return: name of the app as string
        """
        # https://stackoverflow.com/questions/32295395/how-to-get-the-process-name-by-pid-in-linux-using-python
        pid = EWMH.getWmPid(self._hWnd)
        with subprocess.Popen(f"ps -q {pid} -o comm=", shell=True, stdout=subprocess.PIPE) as p:
            ret = p.communicate()
        if len(ret) > 0:
            ret = ret[0].decode(encoding="utf8").replace("\n", "")
        return ret

    def getParent(self) -> Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]:
        """
        Get the handle of the current window parent. It can be another window or an application

        :return: handle of the window parent
        """
        return self._hWnd.query_tree().parent

    def getChildren(self) -> List[int]:
        """
        Get the children handles of current window

        :return: list of handles
        """
        w = DISP.create_resource_object('window', self._hWnd)
        return w.query_tree().children

    def getHandle(self) -> Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]:
        """
        Get the current window handle

        :return: window handle
        """
        return self._hWnd

    def isParent(self, child: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]) -> bool:
        """Returns ''True'' if the window is parent of the given window as input argument

        Args:
        ----
            ''child'' handle of the window you want to check if the current window is parent of
        """
        return child.query_tree().parent == self._hWnd
    isParentOf = isParent  # isParentOf is an alias of isParent method

    def isChild(self, parent: Union[Cursor, Drawable, Pixmap, Resource, Fontable, Window, GC, Colormap, Font]) -> bool:
        """
        Check if current window is child of given window/app (handle)

        :param parent: handle of the window/app you want to check if the current window is child of
        :return: ''True'' if current window is child of the given window
        """
        return parent == self.getParent()
    isChildOf = isChild  # isParentOf is an alias of isParent method

    @property
    def isMinimized(self) -> bool:
        """
        Check if current window is currently minimized

        :return: ``True`` if the window is minimized
        """
        state = EWMH.getWmState(self._hWnd, str=True)
        return STATE_HIDDEN in state

    @property
    def isMaximized(self) -> bool:
        """
        Check if current window is currently maximized

        :return: ``True`` if the window is maximized
        """
        state = EWMH.getWmState(self._hWnd, str=True)
        return STATE_MAX_VERT in state and STATE_MAX_HORZ in state

    @property
    def isActive(self) -> bool:
        """
        Check if current window is currently the active, foreground window

        :return: ``True`` if the window is the active, foreground window
        """
        win = EWMH.getActiveWindow()
        return win == self._hWnd

    @property
    def title(self) -> str:
        """
        Get the current window title, as string

        :return: title as a string
        """
        # TODO: detect if title changes: https://stackoverflow.com/questions/23786289/how-to-correctly-detect-application-name-when-changing-focus-event-occurs-with
        name = EWMH.getWmName(self._hWnd)
        if isinstance(name, bytes):
            name = name.decode()
        return name

    @property
    def visible(self) -> bool:
        """
        Check if current window is visible (minimized windows are also visible)

        :return: ``True`` if the window is currently visible
        """
        win = DISP.create_resource_object('window', self._hWnd)
        state = win.get_attributes().map_state
        return state == Xlib.X.IsViewable

    isVisible = visible  # isVisible is an alias for the visible property.

    @property
    def _isMapped(self) -> bool:
        # Returns ``True`` if the window is currently mapped
        win = DISP.create_resource_object('window', self._hWnd)
        state = win.get_attributes().map_state
        return state != Xlib.X.IsUnmapped


def getMousePos() -> Point:
    """
    Get the current (x, y) coordinates of the mouse pointer on screen, in pixels

    :return: Point struct
    """
    mp = ROOT.query_pointer()
    return Point(mp.root_x, mp.root_y)

cursor = getMousePos  # cursor is an alias for getMousePos


def getScreenSize() -> Size:
    """
    Get the width and height of the screen, in pixels

    :return: Size struct
    """
    res = EWMH.getDesktopGeometry()
    return Size(res[0], res[1])

resolution = getScreenSize  # resolution is an alias for getScreenSize


def getWorkArea() -> Rect:
    """
    Get the Rect struct (left, top, right, bottom) of the working (usable by windows) area of the screen, in pixels

    :return: Rect struct
    """
    work_area = EWMH.getWorkArea()
    x = work_area[0]
    y = work_area[1]
    w = work_area[2]
    h = work_area[3]
    return Rect(x, y, x + w, y + h)


def displayWindowsUnderMouse(xOffset: int = 0, yOffset: int = 0) -> None:
    """
    This function is meant to be run from the command line. It will
    automatically display the position of mouse pointer and the titles
    of the windows under it
    """
    if xOffset != 0 or yOffset != 0:
        print('xOffset: %s yOffset: %s' % (xOffset, yOffset))
    try:
        prevWindows = None
        while True:
            x, y = getMousePos()
            positionStr = 'X: ' + str(x - xOffset).rjust(4) + ' Y: ' + str(y - yOffset).rjust(4) + '  (Press Ctrl-C to quit)'
            windows = getWindowsAt(x, y)
            if windows != prevWindows:
                print('\n')
                prevWindows = windows
                for win in windows:
                    name = win.title
                    eraser = '' if len(name) >= len(positionStr) else ' ' * (len(positionStr) - len(name))
                    sys.stdout.write(name + eraser + '\n')
            sys.stdout.write(positionStr)
            sys.stdout.write('\b' * len(positionStr))
            sys.stdout.flush()
            time.sleep(0.3)
    except KeyboardInterrupt:
        sys.stdout.write('\n\n')
        sys.stdout.flush()


def main():
    """Run this script from command-line to get windows under mouse pointer"""
    print("PLATFORM:", sys.platform)
    print("SCREEN SIZE:", resolution())
    print("ALL WINDOWS", getAllTitles())
    npw = getActiveWindow()
    print("ACTIVE WINDOW:", npw.title, "/", npw.box)
    print()
    displayWindowsUnderMouse(0, 0)


if __name__ == "__main__":
    main()
