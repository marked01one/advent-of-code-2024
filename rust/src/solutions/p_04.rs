use chrono::Utc;
use crate::utils::{direction::Direction, file::FileInput};


pub fn template(path: &str) -> (i64, i64, i64) {
    let start = Utc::now();
    let mut a: i64 = 0;
    let mut b: i64  = 0;

    let fp = FileInput::new(path);
    let dir = Direction::new();

    let matrix = fp.read_to_matrix();

    for i in 0..matrix.len() {
        for j in 0..matrix[0].len() {
            if matrix[i][j] == 'X' { 
                for d in dir.to_vec() {
                    a += xmas(&matrix, (i as i32, j as i32), d, 1) as i64
                }
            }

            if (matrix[i][j] == 'A') && (i > 0 && i < matrix.len()-1) && (j > 0 && j < matrix[0].len()-1) { 
                let corners = [
                    matrix[i-1][j-1], matrix[i-1][j+1], matrix[i+1][j-1], matrix[i+1][j+1]
                ];

                if corners.contains(&'X') || corners.contains(&'A') { continue; }

                if corners[0] == corners[3] || corners[1] == corners[2] { continue; }
                
                b += 1;
            }
        }
    }

    let span = (Utc::now()-start)
        .num_microseconds()
        .expect("Unable to get microsecond time delta!");

    return (a, b, span);
}


fn xmas(mat: &Vec<Vec<char>>, src: (i32, i32), dir: (i32, i32), step: i32) -> bool {
    let dest: (i32, i32) = (src.0 + dir.0*step, src.1 + dir.1*step);

    if dest.0 < 0 || dest.0 >= (mat.len() as i32) { return false }
    if dest.1 < 0 || dest.1 >= (mat[0].len() as i32) { return false }

    let (dx, dy) = (dest.0 as usize, dest.1 as usize); 

    match step {
        0 => return mat[dx][dy] == 'X' && xmas(mat, src, dir, step+1),
        1 => return mat[dx][dy] == 'M' && xmas(mat, src, dir, step+1),
        2 => return mat[dx][dy] == 'A' && xmas(mat, src, dir, step+1), 
        3 => return mat[dx][dy] == 'S',
        _ => return false
    }
}

