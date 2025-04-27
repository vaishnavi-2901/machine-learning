package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.example.demo.Manager.SplitWiseManager;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SplitWiseManager splitWiseManager = new SplitWiseManager();
		System.out.println("Hello World!");
	}

}
