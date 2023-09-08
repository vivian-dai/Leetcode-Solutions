class MyHashSet() {
    var fakeSet: BooleanArray = BooleanArray(1000001);

    fun add(key: Int) {
        fakeSet[key] = true;
    }

    fun remove(key: Int) {
        fakeSet[key] = false;
    }

    fun contains(key: Int): Boolean {
        return fakeSet[key];
    }

}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
 