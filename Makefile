now: testing

testing:
	echo "<xml> testing <attrib> hello </attrib> </xml>" > /tmp/dump.xml
	./main.py /tmp/dump.xml
