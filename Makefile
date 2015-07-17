run:
	if [ ! -d engine/bin/com ]; \
	then \
		mkdir -p engine/bin; \
		cd engine/ && javac -d bin/ `find ./ -name '*.java' -regex '^[./A-Za-z0-9]*$$'`; \
	fi;
	cd engine/ && java -cp bin com.theaigames.game.texasHoldem.TexasHoldem "python $(CURDIR)/deep_green/bot.py --debug" "python $(CURDIR)/deep_green/template_bot.py" 2>../err.log 1>../out.log

zip:
	rm bot.zip && cd deep_green/ && zip -r ../bot.zip * -x *.pyc -x *~ -x template_bot.py -x static_hole/generate_data.py

test:
	cd deep_green/ && python test_utils.py
