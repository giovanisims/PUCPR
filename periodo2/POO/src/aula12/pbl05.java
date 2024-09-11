package aula12;

import java.util.ArrayList;
import java.util.Scanner;

public class pbl05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Creating Students
        Student student1 = new Student("Alice", 20, "alice@example.com", "S001", "Computer Science");
        Student student2 = new Student("Bob", 22, "bob@example.com", "S002", "Mathematics");
        Student student3 = new Student("Charlie", 21, "charlie@example.com", "S003", "Physics");
        Student student4 = new Student("Diana", 23, "diana@example.com", "S004", "Chemistry");

        // Creating Teachers
        Teacher teacher1 = new Teacher("Eve", 40, "eve@example.com", 5000.0, "Biology");
        Teacher teacher2 = new Teacher("Frank", 45, "frank@example.com", 5500.0, "History");

        // Creating Employees
        Employee employee1 = new Employee("Grace", 30, "grace@example.com", "Admin", 40, 20.0);
        Employee employee2 = new Employee("Hank", 35, "hank@example.com", "Maintenance", 40, 15.0);
        Employee employee3 = new Employee("Ivy", 28, "ivy@example.com", "Library", 40, 18.0);
        Employee employee4 = new Employee("Jack", 32, "jack@example.com", "IT", 40, 25.0);
        Employee employee5 = new Employee("Karen", 29, "karen@example.com", "Cafeteria", 40, 12.0);

        // Creating Monitor
        Monitor monitor1 = new Monitor("Leo", 24, "leo@example.com", 20);

        // Makes list of everyone
        ArrayList<Person> employees = new ArrayList<>();
        employees.add(student1);
        employees.add(student2);
        employees.add(student3);
        employees.add(student4);
        employees.add(teacher1);
        employees.add(teacher2);
        employees.add(employee1);
        employees.add(employee2);
        employees.add(employee3);
        employees.add(employee4);
        employees.add(employee5);
        employees.add(monitor1);

        while (true) {
            System.out.println("""
                    ********* Menu *********
                    (1) Ver detalhes do funcionário
                    (2) Sair
                    """);
            System.out.print("Opção: ");
            int option = sc.nextInt();
            sc.nextLine(); // Consume newline

            switch (option) {
                case 1:
                    System.out.print("Digite o nome do funcionário: ");
                    String name = sc.nextLine();
                    System.out.printf("Tem certeza que deseja ver os detalhes de: %s%n", name);
                    String confirmation = sc.nextLine();
                    if (confirmation.equalsIgnoreCase("sim")) {
                        displayEmployeeDetails(employees, name);
                    } else {
                        System.out.println("Voltando...");
                    }
                    break;
                case 2:
                    System.out.println("Saindo...");
                    sc.close();
                    return;
                default:
                    System.out.println("Opção Inválida. Tente novamente.");
                    break;
            }
        }
    }

    public static void displayEmployeeDetails(ArrayList<Person> employees, String name) {
        for (Person employee : employees) {
            if (employee.getName().equalsIgnoreCase(name)) {
                System.out.println(employee);
                return;
            }
        }
        System.out.println("Funcionário não encontrado.");
    }
}

class Person {
    private final String name;
    private int age;
    private final String email;

    protected Person(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public String toString() {
        return String.format("Nome: %s | Idade: %d | Email: %s", this.name, this.age, this.email);
    }
}

class Student extends Person {
    private final String studentID;
    private final String course;

    Student(String name, int age, String email, String studentID, String subject) {
        super(name, age, email);
        this.studentID = studentID;
        this.course = subject;
    }

    public String toString() {
        return String.format(super.toString(), "Matriucula: %s | Curso: %s ", this.studentID, this.course);
    }
}

class Teacher extends Person {
    private final String subject;
    private final double salary;

    Teacher(String name, int age, String email, double wage, String subject) {
        super(name, age, email);
        this.salary = wage;
        this.subject = subject;
    }

    public String toString() {
        return String.format(super.toString(), "Disciplina: %s | Salario: %s ", this.subject, this.salary);
    }

    public String bonus() {
        return String.format("Bônus: %.2f", (this.salary * 1.1));
    }
}

class Employee extends Person {
    private final String department;
    private final int workHours;
    private final double workSalary;

    Employee(String name, int age, String email, String department, int workHours, double workSalary) {
        super(name, age, email);
        this.department = department;
        this.workHours = workHours;
        this.workSalary = workSalary;
    }

    public String calculatePayment() {
        return String.format("Departamento: %s | O pagamento é: %.2f", this.department, this.workHours * this.workSalary);
    }
}

class Monitor extends Person {
    private final int workHours;

    Monitor(String name, int age, String email, int monitorHours) {
        super(name, age, email);
        this.workHours = monitorHours;
    }

    public String toString() {
        return String.format(super.toString(), "Horas de monitoria: %.2f", this.workHours);
    }

    public String calculatePayment() {
        return String.format("O pagamento é: %x", this.workHours * 30);
    }
}