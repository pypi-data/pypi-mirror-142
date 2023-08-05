#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <ranges>
#include <boost/unordered_map.hpp>
#include <map>
#include <cmath>
#include <vector>


int c_dist(const std::pair<int, int>& p1, const std::pair<int, int>& p2) {
    return std::max(std::abs(p2.second - p1.second), std::abs(p2.first - p1.first));
}

std::pair<int, int> pair_add(const std::pair<int, int>& p1, const std::pair<int, int>& p2) {
    return std::make_pair(p1.first + p2.first, p1.second + p2.second);
}

bool isWhiteControlled(const std::pair<int, int>& pos, const std::pair<int, int>& wk_pos, const std::pair<int, int>& rook_pos) {
    if (c_dist(pos, wk_pos) == 1) {
        return true;
    }
    if ((pos.first == rook_pos.first) ^ (pos.second == rook_pos.second)) {
        if (pos.first == rook_pos.first && (wk_pos.first != rook_pos.first || !((pos.second - wk_pos.second) * (wk_pos.second - rook_pos.second) > 0))) {
            return true;
        }
        if (pos.second == rook_pos.second && (wk_pos.second != rook_pos.second || !((pos.first - wk_pos.first) * (wk_pos.first - rook_pos.first) > 0))) {
            return true;
        }
    }
    return false;
}

auto find_black_moves(const std::pair<int, int>& bk_pos, const std::pair<int, int>& wk_pos, const std::pair<int, int>& rook_pos) {
    std::vector<std::pair<int, int>> possible_moves;
    for (int i = -1; i <= 1; ++i) {
        for (int j = -1; j <= 1; ++j) {
            possible_moves.push_back(std::make_pair(i, j));
        }
    }
    std::vector<std::pair<int, int>> move_list;
    for (const auto& i : possible_moves) {
        move_list.push_back(pair_add(i, bk_pos));
    }
    auto in_boundaries = [](std::pair<int, int> x) { return 0 <= x.first && x.first < 8 && 0 <= x.second && x.second < 8; };
    auto not_same_pos = [bk_pos](std::pair<int, int> x) { return x != bk_pos; };
    auto not_controlled = [wk_pos, rook_pos](std::pair<int, int> x) { return !isWhiteControlled(x, wk_pos, rook_pos); };
    auto predicate = [in_boundaries, not_same_pos, not_controlled](std::pair<int, int> x) { return in_boundaries(x) && not_same_pos(x) && not_controlled(x); };

    std::vector<std::pair<int, int>> out;
    std::ranges::copy_if(move_list, std::back_inserter(out), predicate);
    return out;
}

auto find_white_moves(std::pair<int, int>& bk_pos, std::pair<int, int>& wk_pos, std::pair<int, int>& rook_pos) {
    auto in_boundaries = [](std::pair<int, int> x) { return 0 <= x.first && x.first < 8 && 0 <= x.second && x.second < 8; };
    auto not_same_pos = [wk_pos, rook_pos](std::pair<int, int> x) { return x != wk_pos && x != rook_pos; };
    auto not_controlled = [bk_pos](std::pair<int, int> x) { return c_dist(x, bk_pos) > 1; };
    auto predicate = [in_boundaries, not_same_pos, not_controlled](std::pair<int, int> x) { return in_boundaries(x) && not_same_pos(x) && not_controlled(x); };

    std::vector<std::pair<int, int>> possible_moves;
    for (int i = -1; i <= 1; ++i) {
        for (int j = -1; j <= 1; ++j) {
            possible_moves.push_back(std::make_pair(i, j));
        }
    }

    std::vector<std::pair<int, int>> wk_move_list;
    for (const auto& i : possible_moves) {
        wk_move_list.push_back(pair_add(i, wk_pos));
    }
    std::pair<std::vector<std::pair<int, int>>, std::vector<std::pair<int, int>>> out;
    std::ranges::copy_if(wk_move_list, std::back_inserter(out.first), predicate);

    int directions[4][2] = { {1,0}, {0,1}, {-1,0}, {0,-1} };
    std::pair<int, int> pos;

    for (const auto& i : directions) {
        const std::pair<int, int> direction = std::make_pair(i[0], i[1]);
        pos = pair_add(rook_pos, direction);
        while (in_boundaries(pos) && pos != wk_pos) {
            out.second.push_back(pos);
            pos = pair_add(pos, direction);
        }
    }
    return out;
}

template <typename Func, typename Seq>
auto map(Func func, Seq seq) {
    typedef typename Seq::value_type value_type;
    using return_type = decltype(func(std::declval<value_type>()));
    std::vector<return_type> result{};
    for (auto i : seq | std::ranges::views::transform(func)) result.push_back(i);
    return result;
}

auto find_transform(std::pair<int, int>& bk_pos, std::pair<int, int>& wk_pos, std::pair<int, int>& rook_pos) {
    auto flip_over_y = [](std::pair<int, int> x) { return std::make_pair(x.first, 7 - x.second); };
    auto flip_over_x = [](std::pair<int, int> x) { return std::make_pair(7 - x.first, x.second); };
    auto flip_anti_diagonal = [](std::pair<int, int> x) { return std::make_pair(x.second, x.first); };
    auto flip_diagonal = [](std::pair<int, int> x) { return std::make_pair(7 - x.second, 7 - x.first); };
    std::vector<std::pair<int, int>> positions = { bk_pos, wk_pos, rook_pos };
    if (bk_pos.second < 4) {
        if (bk_pos.first > 3) {
            positions = map(flip_anti_diagonal, positions);
        }
        else {
            positions = map(flip_over_y, positions);
        }
    }
    else {
        if (bk_pos.first > 3) {
            positions = map(flip_over_x, positions);
        }
    }
    if (positions[0].first < (7 - positions[0].second)) {
        positions = map(flip_diagonal, positions);
    }
    return positions;
}

auto generate_valid_states() {
    std::vector<std::pair<int, int>> all_positions;
    std::vector<std::vector<std::pair<int, int>>> valid_states;
    for (int i = 0; i <= 7; ++i) {
        for (int j = 0; j <= 7; ++j) {
            all_positions.push_back(std::make_pair(i, j));
        }
    }

    for (const auto& i : all_positions) {
        if (i.second > 3 && i.first < 4 && i.first >= 7 - i.second) {
            for (const auto& j : all_positions) {
                for (const auto& k : all_positions) {
                    if (i != j && j != k && i != k) {
                        valid_states.push_back(std::vector<std::pair<int, int>>{i, j, k});
                    }
                }
            }
        }
    }
    auto king_space = [](std::vector<std::pair<int, int>> x) { return c_dist(x[0], x[1]) > 1; };
    auto quad_zero = [](std::vector<std::pair<int, int>> x) { return x[0].second > 3 && x[0].first < 4 && x[0].first >= 7 - x[0].second; };
    auto predicate = [king_space, quad_zero](std::vector<std::pair<int, int>> x) { return king_space(x) && quad_zero(x); };
    std::vector<std::vector<std::pair<int, int>>> out_states;
    std::ranges::copy_if(valid_states, std::back_inserter(out_states), predicate);

    return out_states;
}

auto get_white_valid_states() {
    std::vector<std::vector<std::pair<int, int>>> out;
    auto valid_states = generate_valid_states();
    auto unpack_white_control = [](std::vector<std::pair<int, int>> x) { return isWhiteControlled(x[0], x[1], x[2]); };
    std::remove_copy_if(begin(valid_states), end(valid_states), std::back_inserter(out), unpack_white_control);
    return out;
}

auto determine_game_state(const std::pair<int, int>& bk_pos, const std::pair<int, int>& wk_pos, const std::pair<int, int>& rook_pos, const bool turn) {
    if (bk_pos == rook_pos) {
        return 100;
    }
    if (!turn && find_black_moves(bk_pos, wk_pos, rook_pos).empty()) {
        if (isWhiteControlled(bk_pos, wk_pos, rook_pos)) {
            return 0;
        }
        return 100;
    }
    return -1;
}

boost::unordered_map<std::pair<std::vector<std::pair<int, int>>, bool>, int> memo_dict;
boost::unordered_map<std::pair<std::vector<std::pair<int, int>>, bool>, int> depth_dict;

auto minimax(std::pair<int, int> bk_pos, std::pair<int, int> wk_pos, std::pair<int, int> rook_pos, bool turn, int depth = 0) {
    auto transformed_positions = find_transform(bk_pos, wk_pos, rook_pos);
    bk_pos = transformed_positions[0];
    wk_pos = transformed_positions[1];
    rook_pos = transformed_positions[2];
    std::pair<std::vector<std::pair<int, int>>, bool> position;
    position = std::make_pair(transformed_positions, turn);
    if (::memo_dict.find(position) != ::memo_dict.end()) {
        if (::depth_dict[position] >= depth) {
            return ::memo_dict[position];
        }
    }
    auto game_state = determine_game_state(bk_pos, wk_pos, rook_pos, turn);
    if (game_state != -1) {
        ::memo_dict[position] = game_state;
        ::depth_dict[position] = 100;
        return game_state;
    }
    if (depth == 0) {
        if (::depth_dict.find(position) == ::depth_dict.end()) {
            ::depth_dict[position] = 0;
            ::memo_dict[position] = 100;
        }
        return 100;
    }
    if (turn) {
        int min_val = 200;
        auto white_mvs = find_white_moves(bk_pos, wk_pos, rook_pos);
        auto& wk_moves = white_mvs.first;
        auto& rook_moves = white_mvs.second;
        for (const auto& wk_move : wk_moves) {
            min_val = std::min(min_val, minimax(bk_pos, wk_move, rook_pos, !turn, depth - 1) + 1);
        }
        for (const auto& rook_move : rook_moves) {
            min_val = std::min(min_val, minimax(bk_pos, wk_pos, rook_move, !turn, depth - 1) + 1);
        }
        if (::depth_dict.find(position) != ::depth_dict.end()) {
            if (depth > ::depth_dict[position]) {
                ::depth_dict[position] = depth;
                ::memo_dict[position] = min_val;
            }
        }
        else {
            ::depth_dict[position] = depth;
            ::memo_dict[position] = min_val;
        }
        return min_val;
    }
    int max_val = -100;
    auto bk_moves = find_black_moves(bk_pos, wk_pos, rook_pos);
    for (auto& bk_move : bk_moves) {
        max_val = std::max(max_val, minimax(bk_move, wk_pos, rook_pos, !turn, depth - 1) + 1);
    }
    if (::depth_dict.find(position) != ::depth_dict.end()) {
        if (depth > ::depth_dict[position]) {
            ::depth_dict[position] = depth;
            ::memo_dict[position] = max_val;
        }
    }
    else {
        ::depth_dict[position] = depth;
        ::memo_dict[position] = max_val;
    }
    return max_val;
}

std::vector<std::pair<std::vector<std::pair<int, int>>, int>> white_ply;
std::vector<std::pair<std::vector<std::pair<int, int>>, int>> black_ply;

void generate_tablebase() {
    auto white_starting_states = get_white_valid_states();
    auto black_starting_states = generate_valid_states();
    for (const auto& state : white_starting_states) {
        auto& bk_pos = state[0];
        auto& wk_pos = state[1];
        auto& rook_pos = state[2];
        ::white_ply.push_back(std::make_pair(state, minimax(bk_pos, wk_pos, rook_pos, true, 32)));
    }
    for (const auto& state : black_starting_states) {
        auto& bk_pos = state[0];
        auto& wk_pos = state[1];
        auto& rook_pos = state[2];
        ::black_ply.push_back(std::make_pair(state, minimax(bk_pos, wk_pos, rook_pos, false, 32)));
    }
}


auto get_lists() {
    generate_tablebase();
    std::map<std::tuple<std::pair<int, int>, std::pair<int, int>, std::pair<int, int>>, int> black_ply;
    std::map<std::tuple<std::pair<int, int>, std::pair<int, int>, std::pair<int, int>>, int> white_ply;

    return std::make_pair(::black_ply, ::white_ply);
}

int main() {

    // generate_tablebase();

}

namespace py = pybind11;

PYBIND11_MODULE(tablebase, m) {
    m.def("get_lists", &get_lists, R"pbdoc(
        get the lists containing the tablebases.
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}