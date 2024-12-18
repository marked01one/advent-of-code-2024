mod solutions;
mod utils;

use solutions::{p_01, p_02, p_03, p_04};

fn main() {
    let (a_01, b_01, time_01) = p_01::template("../../01.txt");
    let (a_02, b_02, time_02) = p_02::template("../../02.txt");
    let (a_03, b_03, time_03) = p_03::template("../../03.txt");
    let (a_04, b_04, time_04) = p_04::template("../../04.txt");
    
    println!("RESULTS");
    println!("* 01: ({a_01}, {b_01})\t[{} ms]", (time_01 as f64) / 1000.0);
    println!("* 02: ({a_02}, {b_02})\t\t[{} ms]", (time_02 as f64) / 1000.0);
    println!("* 03: ({a_03}, {b_03})\t[{} ms]", (time_03 as f64) / 1000.0);
    println!("* 04: ({a_04}, {b_04})\t\t[{} ms]", (time_04 as f64) / 1000.0);
}
