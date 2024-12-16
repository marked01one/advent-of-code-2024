mod solutions;


fn main() {
    let (a_01, b_01) = solutions::p_01::template("../../01.txt");
    let (a_02, b_02) = solutions::p_02::template("../../02.txt");
    
    println!("RESULTS");
    println!("* 01: ({}, {})", a_01, b_01);
    println!("* 02: ({}, {})", a_02, b_02);
}
