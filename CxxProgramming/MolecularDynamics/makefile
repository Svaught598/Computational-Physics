SRC=./src/
INC=./include/
OUT=./out/


all: main

main: particlegod.o $(SRC)main.cpp
	g++ particlegod.o -g -o $(OUT)main.exe $(SRC)main.cpp 

particlegod.o: $(INC)particle.hpp $(INC)particlegod.hpp 
	g++ -g -c $(SRC)particlegod.cpp 
	
# shortcut commands
clean:
	rm ./*.o 

fuck:
	rm ./out/*.txt ./out/*.png

run:
	./out/main.exe

plot: 
	./out/main.exe --plot

show:
	xdg-open ./out/particle.mp4