#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/chunchih/final_proj/src/final_project/rotors_evaluation"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/chunchih/final_proj/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/chunchih/final_proj/install/lib/python3/dist-packages:/home/chunchih/final_proj/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/chunchih/final_proj/build" \
    "/usr/bin/python3" \
    "/home/chunchih/final_proj/src/final_project/rotors_evaluation/setup.py" \
     \
    build --build-base "/home/chunchih/final_proj/build/final_project/rotors_evaluation" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/chunchih/final_proj/install" --install-scripts="/home/chunchih/final_proj/install/bin"
