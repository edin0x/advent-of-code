import { readInput } from "../../read-input";
import { solve1, solve2 } from "./1";

const fs = require("fs");

describe("2022/1/1", () => {
  it("should give correct result for sample", async () => {
    expect(solve1("2022/1/input_sample")).toEqual(24000);
  });

  it("should give correct result for input", async () => {
    expect(solve1("2022/1/input")).toEqual(66186);
  });
});

describe("2022/1/2", () => {
  it("should give correct result for sample", async () => {
    expect(solve2("2022/1/input_sample")).toEqual(45000);
  });

  it("should give correct result for input", async () => {
    expect(solve2("2022/1/input")).toEqual(196804);
  });
});
