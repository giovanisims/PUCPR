package arrayList;

public class ArrayList<T> {

    protected T[] data;
    protected int capacity;

    protected ArrayList() {}
    protected ArrayList(int capacity) {}
    protected void add(T e) {}
    protected void add(int index, T e) {}
    protected void remove(int index) {}
    protected void remove(T o) {}
    protected T set(int index, T e) {return null;}
    protected T get(int index) {return null;}
    protected boolean contains(T o) {return false;}
    protected int indexOf(T o) {return 0;}
    protected T[] toArray() {return data;}
}
