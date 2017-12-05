-- ghc -o day4 day4.hs
import Data.List(sort)
import qualified Data.Set as Set
import System.IO

main = do
    contents <- readFile "input"
    let ls = map words (lines contents)
        lss = map (map sort) ls
        isValid l = if length l == length (Set.fromList l) then 1 else 0
        calc xs = show (foldl (+) 0 (map isValid xs))
    print $ "Answer part 1: " ++ calc ls
    print $ "Answer part 2: " ++ calc lss
