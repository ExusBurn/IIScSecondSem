# ========================
# Compiler settings
# ========================
CXX := g++
CXXFLAGS := -std=c++17 -O2 -Wall

# ========================
# Target
# ========================
TARGET := q2_solver

# ========================
# Default target
# ========================
all: run

# ========================
# Build
# ========================
$(TARGET): main.cpp arange.cpp Euler_fwd_bwd_rk4.cpp
	$(CXX) $(CXXFLAGS) $^ -o $@

# ========================
# Run
# ========================
run: $(TARGET)
	./$(TARGET)

# ========================
# Clean
# ========================
clean:
	rm -f $(TARGET)
	rm -f *.txt
