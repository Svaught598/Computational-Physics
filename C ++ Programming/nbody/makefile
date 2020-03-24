SRC=./src/
INC=./include/
OUT=./out/


all: main

main: particlegod.o $(SRC)main.cpp
	g++ particlegod.o -o $(OUT)main.exe $(SRC)main.cpp $(INC)gnuplot.hpp

particlegod.o: $(INC)particle.hpp $(INC)particlegod.hpp 
	g++ -g -c $(SRC)particlegod.cpp 


# shortcut commands
clean:
	rm ./*.o

run:
	./out/main.exe
