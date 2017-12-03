public class day3 {
  public static void main(String[] args) {
    int INPUT = 312051;
    int wh = (int) Math.ceil(Math.sqrt(INPUT));
    double[][] matrix = new double[wh+1][wh+1];

    int direction = 0;
    int number_forward = 0;
    int number_forward_times = 0;
    int number_forward_max = 1;

    int center_x, center_y, i, j;
    center_x = center_y = i = j = (int) Math.ceil(wh/2);

    boolean found_part_two = false;

    for (int number = 0; number < INPUT; number++) {
      if (number == INPUT-1) {
        System.out.println("Answer part one: " + (Math.abs(center_x-i) + Math.abs(center_y-j)));
      }

      if (i == center_x && j == center_y) {
        matrix[i][j] = number + 1;
      } else if (!found_part_two) {
        matrix[i][j] =
            matrix[i-1][j-1]
          + matrix[i][j-1]
          + matrix[i+1][j-1]
          + matrix[i+1][j]
          + matrix[i+1][j+1]
          + matrix[i][j+1]
          + matrix[i-1][j+1]
          + matrix[i-1][j];
      }

      if (matrix[i][j] > INPUT) {
          System.out.println("Answer part two: " + (int) matrix[i][j]);
          found_part_two = true;
      }

      if (direction == 0) {
        i += 1;
      } else if (direction == 1) {
        j -= 1;
      } else if (direction == 2) {
        i -= 1;
      } else if (direction == 3) {
        j += 1;
      }

      number_forward += 1;

      if (number_forward == number_forward_max) {
          number_forward = 0;
          number_forward_times += 1;

          direction += 1;
          if (direction == 4) {
              direction = 0;
          }

          if (number_forward_times == 2) {
              number_forward_max += 1;
              number_forward_times = 0;
          }
      }
    }

  }
}
