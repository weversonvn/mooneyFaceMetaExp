all: do
do:
	pip install -r requirements.txt
	sudo apt install libwebkitgtk-1.0-0
	wget https://extras.wxpython.org/wxPython4/extras/linux/gtk3/debian-10/wxPython-4.1.0-cp37-cp37m-linux_x86_64.whl
	pip install wxPython-4.1.0-cp37-cp37m-linux_x86_64.whl
clean:
	rm -rf wxPython-4.1.0-cp37-cp37m-linux_x86_64.whl
