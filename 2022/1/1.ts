import { readInput } from "../../read-input";

export const solve1 = (inputPath: string): number => {
  const data = readInput(inputPath);
  const elves = data.split("\n\n").map((x) => x.split("\n"));

  const sums = elves.map((x) => x.reduce((a, b) => a + Number(b), 0));

  sums.sort((a, b) => b - a);

  return sums[0];
};

export const solve2 = (inputPath: string): number => {
  const data = readInput(inputPath);
  const elves = data.split("\n\n").map((x) => x.split("\n"));

  const sums = elves.map((x) => x.reduce((a, b) => a + Number(b), 0));

  sums.sort((a, b) => b - a);

  return sums[0] + sums[1] + sums[2];
};
