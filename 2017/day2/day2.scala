import scala.io.Source

object Day2 {
  def main(args: Array[String]): Unit = {
    val lines = Source.fromFile("input").getLines.map(_.split("\t").map(_.toInt)).toList

    val answer1 = lines.map(l => l.sorted).map(l => l.last - l.head).sum
    val answer2 = lines.map(l => l.flatMap(a => l.map(b => if (a%b==0) a/b else 0)).filter(_ > 1).sum).sum

    println(s"Answer part one: $answer1")
    println(s"Answer part two: $answer2")
  }
}
