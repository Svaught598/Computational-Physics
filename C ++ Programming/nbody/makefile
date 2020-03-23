SRC=./src/
INC=./include/
OUT=./out/


all: main

main: particle.o particlegod.o $(SRC)main.cpp
	g++ particle.o particlegod.o -o $(OUT)main.exe $(SRC)main.cpp $(INC)gnuplot.hpp

particle.o: $(INC)particle.hpp $(SRC)particle.cpp
	g++ -g -c $(SRC)particle.cpp 

particlegod.o: $(INC)particle.hpp $(INC)particlegod.hpp 
	g++ -g -c $(SRC)particlegod.cpp

clean:
	rm ./*.o

run:
	./out/main.exe