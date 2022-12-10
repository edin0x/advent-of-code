const fs = require("fs");

export const readInput = (path: string): string => {
  return fs.readFileSync(path, "utf8", (err: any, data: any) => {
    if (err) {
      console.error(err);
      return;
    }

    return data;
  });
};
