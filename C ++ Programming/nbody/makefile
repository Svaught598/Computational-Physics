SRC=./src/
INC=./include/
OUT=./out/


all: main

main: particle.o $(SRC)main.cpp
	g++ particle.o -o $(OUT)main.exe $(SRC)main.cpp $(INC)gnuplot.hpp

particle.o: $(INC)particle.hpp $(SRC)particle.cpp
	g++ -g -c $(SRC)particle.cpp 

clean:
	rm ./*.o