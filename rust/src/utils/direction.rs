pub struct Direction {
    n: (i32, i32),
    s: (i32, i32),
    e: (i32, i32),
    w: (i32, i32),
    nw: (i32, i32),
    ne: (i32, i32),
    sw: (i32, i32),
    se: (i32, i32)
}

impl Direction {
    pub fn new() -> Self {
        Direction {
            n: (-1, 0),
            s: (1, 0),
            w: (0, -1),
            e: (0, 1),
            nw: (-1, -1),
            ne: (-1, 1),
            sw: (1, -1),
            se: (1, 1)
        }
    }
    pub fn to_vec(&self) -> Vec<(i32, i32)> {
        return vec![
            self.n, self.s, self.e, self.w,
            self.nw, self.ne, self.sw, self.se
        ];
    }
}