import os
import time

import Xlib
import ewmh
import pywinctl
from pynput import mouse

DISP = Xlib.display.Display()
SCREEN = DISP.screen()
ROOT = DISP.screen().root
EWMH = ewmh.EWMH(_display=DISP, root=ROOT)


def sendBehind(hWnd):

    w = DISP.create_resource_object('window', hWnd)
    w.change_property(DISP.intern_atom('_NET_WM_STATE', False), Xlib.Xatom.ATOM, 32, [DISP.intern_atom('_NET_WM_STATE_BELOW', False), ], Xlib.X.PropModeReplace)
    w.change_property(DISP.intern_atom('_NET_WM_STATE', False), Xlib.Xatom.ATOM, 32, [DISP.intern_atom('_NET_WM_STATE_SKIP_TASKBAR', False), ], Xlib.X.PropModeAppend)
    w.change_property(DISP.intern_atom('_NET_WM_STATE', False), Xlib.Xatom.ATOM, 32, [DISP.intern_atom('_NET_WM_STATE_SKIP_PAGER', False), ], Xlib.X.PropModeAppend)
    DISP.flush()

    # This sends window below all others, but not behind the desktop icons
    w.change_property(DISP.intern_atom('_NET_WM_WINDOW_TYPE', False), Xlib.Xatom.ATOM, 32, [DISP.intern_atom('_NET_WM_WINDOW_TYPE_DESKTOP', False), ],Xlib.X.PropModeReplace)
    DISP.flush()

    if "GNOME" in os.environ.get('XDG_CURRENT_DESKTOP', ""):
        # This sends the window "too far behind" (below all others, including Wallpaper, like unmapped)
        # Trying to figure out how to raise it on top of wallpaper but behind desktop icons
        desktop = _xlibGetAllWindows(title="gnome-shell")
        if desktop:
            w.reparent(desktop[-1], 0, 0)
            DISP.flush()
    else:
        # Mint/Cinnamon: just clicking on the desktop, it raises, sending the window/wallpaper to the bottom!
        m = mouse.Controller()
        m.move(SCREEN.width_in_pixels - 1, 100)
        m.click(mouse.Button.left, 1)

    return '_NET_WM_WINDOW_TYPE_DESKTOP' in EWMH.getWmWindowType(hWnd, str=True)


def bringBack(hWnd, parent):
    w = DISP.create_resource_object('window', hWnd)

    if parent:
        w.reparent(parent, 0, 0)
        DISP.flush()

    w.unmap()
    w.change_property(DISP.intern_atom('_NET_WM_WINDOW_TYPE', False), Xlib.Xatom.ATOM,
                      32, [DISP.intern_atom('_NET_WM_WINDOW_TYPE_NORMAL', False), ],
                      Xlib.X.PropModeReplace)
    DISP.flush()
    w.change_property(DISP.intern_atom('_NET_WM_STATE', False), Xlib.Xatom.ATOM,
                      32, [DISP.intern_atom('_NET_WM_STATE_FOCUSED', False), ],
                      Xlib.X.PropModeReplace)
    DISP.flush()
    w.map()
    EWMH.setActiveWindow(hWnd)
    EWMH.display.flush()
    return '_NET_WM_WINDOW_TYPE_NORMAL' in EWMH.getWmWindowType(hWnd, str=True)


def _xlibGetAllWindows(parent: int = None, title: str = ""):

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


hWnd = pywinctl.getActiveWindow()
parent = hWnd._hWnd.query_tree().parent
sendBehind(hWnd._hWnd)
time.sleep(3)
bringBack(hWnd._hWnd, parent)
