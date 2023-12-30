use std::fs;

pub fn run(path: &str) -> i32 {
    println!("Reading file: {path}");
    let contents = fs::read_to_string(path)
        .expect("Couldn't read file {path}");

    let board = create_board(&contents);
    dbg!("Board: ", &board);
    let mut sum = 0;

    for (idx, row) in board.iter().enumerate() {
        for (jdx, e) in row.iter().enumerate() {
            if e.is_digit(10) {
                continue;
            }

            if e != &'.' {
                // Check the surrounding indices
                sum += find_neighbors(&board, idx, jdx);
            }
        }
    }

    sum
}


fn find_neighbors(board: &Vec<Vec<char>>, i: usize, j: usize) -> i32 {
    dbg!("Found special character at", i, j);
    let mut num_list: Vec<i32> = Vec::new();
    for k in i-1..i+2 {
        for l in j-1..j+2 {
            match board.get(k) {
                Some(row) => {
                    match row.get(l) {
                        Some(e) => {
                            if e.is_digit(10) {
                                num_list = add_num(num_list, &row, l);
                            }
                        },
                        None => continue,
                    }
                },
                None => continue,
            }
        }
    }

    num_list.iter().sum()
}

fn add_num(mut nums: Vec<i32>, row: &Vec<char>, idx: usize) -> Vec<i32> {
    dbg!("Found number, building full length");
    let mut lower = idx;
    for l in (0..idx).rev() {
        match row.get(l) {
            Some(e) => {
                if e.is_digit(10) {
                    lower = l;
                } else {
                    break;
                }
            },
            None => break,
        }
    }

    let mut upper = idx;
    for u in idx..row.len() {
        match row.get(u) {
            Some(e) => {
                if e.is_digit(10) {
                    upper = u;
                } else {
                    break;
                }
            },
            None => break,
        }
    }

    let num = row[lower..upper+1].iter().collect::<String>();
    dbg!(row);
    dbg!(lower, upper);
    if num.len() != 0 {
        let num = num.parse::<i32>().unwrap();
        dbg!(num);

        if !nums.contains(&num) {
            nums.push(num);
        }
    }

    nums
}

fn create_board(contents: &String) -> Vec<Vec<char>> {
    let mut board: Vec<Vec<char>> = Vec::new();

    for line in contents.lines() {
        let mut row: Vec<char> = Vec::new();

        for chr in line.chars() {
            row.push(chr);
        }

        board.push(row);
    }
    // dbg!("Board: {}", board);

    board
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sample() {
        let f_in = "sample.txt";
        assert_eq!(run(f_in), 4361);
    }
}
