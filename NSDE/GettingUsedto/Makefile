# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -Wall -O2 -fopenmp

# Target executable
TARGET = hello

# Source files
SRC = hello.cpp

# Default target
all: $(TARGET)

# Build rule
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET)

# Run the program
run: $(TARGET)
	./$(TARGET)

# Clean build files
clean:
	rm -f $(TARGET)
