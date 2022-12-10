import { readInput } from "../../read-input";
import { solve1, solve2 } from "./1";

const fs = require("fs");

const day = "0";

describe("2022/1/1", () => {
  it("should give correct result for sample", async () => {
    expect(solve1(`2022/${day}/input_sample`)).toEqual(0);
  });

  it("should give correct result for input", async () => {
    expect(solve1(`2022/${day}/input`)).toEqual(0);
  });
});

describe("2022/1/2", () => {
  it("should give correct result for sample", async () => {
    expect(solve2(`2022/${day}/input_sample`)).toEqual(0);
  });

  it("should give correct result for input", async () => {
    expect(solve2(`2022/${day}/input`)).toEqual(0);
  });
});
