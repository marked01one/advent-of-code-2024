mod solutions;

use solutions::p_01;

fn main() {
    let (a_01, b_01) = p_01::template("../../01.txt");
    
    println!("Result: ({}, {})", a_01, b_01);
}
