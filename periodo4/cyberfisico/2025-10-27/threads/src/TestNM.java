import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class TestNM {

    public static void simulateNModel(int numTasks, int poolSize) {
        System.out.println("--- Simulating " + numTasks + " tasks on " + poolSize + " threads ---");

        // po0lSize is the amount of threads in a system that we get from availableProcessors() in the RunTests file
        // using a thread pool means that the amount of threads is going to be constant, but it's better for performance
        // since reusing threads means less overhead than creating and destroying them.
        // ExecutorService manages the allocation of tasks to the threadpool, and it functions like an API
        // it manages everything from the task queue to shutting down the threads cleanly
        // there are ways to implement executor with more parameters for extra control or even manage everything manually
        // but there is no need here and managing them manually is actually not recommended.
        ExecutorService executor = Executors.newFixedThreadPool(poolSize);

        long startTime = System.currentTimeMillis();

        // Create a task object and adds them to the task queue in executor
        for (int i = 0; i < numTasks; i++) {
            executor.submit(new Task());
        }

        // This starts the shutdown of the tasks, not accepting new tasks, but it lets the tasks in the background continue running
        executor.shutdown();

        // So we need awaitTermination() otherwise the code would drop from the bottom and finish counting the time before it finished all the tasks
        try {
            executor.awaitTermination(100, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        long endTime = System.currentTimeMillis();
        System.out.println("Total Time: " + (endTime - startTime) + " ms");
    }
}

