import java.util.ArrayList;
import java.util.List;

public class Test11 {

    public static void simulate11Model(int threadCount) {
        System.out.println("--- Simulating " + threadCount + " threads ---");

        // Technically we don't need to add the threads to an array and then start them, but it makes a more accurate benchmark if we do
        List<Thread> threads = new ArrayList<>();
        for (int i = 0; i < threadCount; i++) {
            Task task = new Task();
            threads.add(new Thread(task));
        }

        long startTime = System.currentTimeMillis();

        for (Thread thread : threads) {
            thread.start();
        }

        // We join all the threads so that the main thread doesn't skip ahead and end the timer early
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Total Time: " + (endTime - startTime) + " ms");
    }

}
