#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

long long MaxPairwiseProductFast(const std::vector<int>& numbers){
    long long max_number = 0;
    int max_index_1 = -1;
    int max_index_2 = -1;
    int n = numbers.size();

    for (int first = 0; first < n; ++first){
        if((max_index_1 == -1) || (numbers[first] > numbers[max_index_1]))
            max_index_1 = first;
    }
    for (int second = 0; second < n; ++second){
        if((second != max_index_1) && ((max_index_2 == -1) || (numbers[second] > numbers[max_index_2])))
            max_index_2 = second;
    }
    max_number = ((long long) (numbers[max_index_1])) * numbers[max_index_2];
    return max_number;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    long long result = MaxPairwiseProductFast(numbers);
    std::cout << result << "\n";
    return 0;
}
