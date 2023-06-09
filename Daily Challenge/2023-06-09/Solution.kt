class Solution {
    fun nextGreatestLetter(letters: CharArray, target: Char): Char {
        var changed = false;
        var smallest = target;
        for(letter in letters) {
            // println("$letter $changed");
            if((!changed && letter > smallest) || (changed && letter < smallest)) {
                smallest = letter;
                changed = true;
            }
        }
        if(!changed) {
            return letters[0];
        } else {
            return smallest;
        }
    }
}
