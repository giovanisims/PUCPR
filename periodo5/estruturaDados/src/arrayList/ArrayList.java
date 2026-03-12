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
    protected void set(int index, T e) { data[index] = e; }
    protected T get(int index) { return data[index]; }

    protected boolean contains(T o) {
        for (T element : data) {
            if (o != null && o.equals(element)) {return true;}} return false;
    }

    protected int indexOf(T o) {
        for (int index = 0; index < data.length; index++) { if (o != null && o.equals(data[index])) { return index; }} return -1;
    }

    protected T[] toArray() { return data; }
}
