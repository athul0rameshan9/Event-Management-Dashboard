package com.Events.EventManagement.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Data
@Table(name = "users")
public class Users {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password;

    public Users(String name, String email, String password) {
        this.name = name;
        this.email = email;
        this.password = password;
    }

    public int id() {
        return id;
    }

    public Users setId(int id) {
        this.id = id;
        return this;
    }

    public String name() {
        return name;
    }

    public Users setName(String name) {
        this.name = name;
        return this;
    }

    public String email() {
        return email;
    }

    public Users setEmail(String email) {
        this.email = email;
        return this;
    }

    public String password() {
        return password;
    }

    public Users setPassword(String password) {
        this.password = password;
        return this;
    }
}
