#include <iostream>
#include <string>

int main() {
    int num_names;
    std::cin >> num_names;
        std::cin.ignore();

    for (int i = 0; i < num_names; i++) {
        std::string name;
        std::getline(std::cin, name);
        std::cout << "Hello, " << name << "!" << std::endl;
    }

    return 0;
}