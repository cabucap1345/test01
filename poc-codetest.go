package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

// Struct để parse JSON response (ví dụ)
type ApiResponse struct {
	Message string `json:"message"`
}

func main() {
	// ========================
	// Example 1: Bearer Token Auth
	// ========================
	url := "https://api.example.com/data"
	token := "your_api_token_here"

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}
	req.Header.Set("Authorization", "Bearer "+token)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)

	if resp.StatusCode == 200 {
		var result ApiResponse
		json.Unmarshal(body, &result)
		fmt.Println("Bearer Auth OK:", result)
	} else {
		fmt.Println("Error:", resp.StatusCode, string(body))
	}

	// ========================
	// Example 2: Basic Auth (username/password)
	// ========================
	url2 := "https://api.example.com/secure-data"
	username := "your_username"
	password := "your_password"

	req2, err := http.NewRequest("GET", url2, nil)
	if err != nil {
		panic(err)
	}
	req2.SetBasicAuth(username, password)

	resp2, err := client.Do(req2)
	if err != nil {
		panic(err)
	}
	defer resp2.Body.Close()

	body2, _ := ioutil.ReadAll(resp2.Body)

	if resp2.StatusCode == 200 {
		var result2 ApiResponse
		json.Unmarshal(body2, &result2)
		fmt.Println("Basic Auth OK:", result2)
	} else {
		fmt.Println("Error:", resp2.StatusCode, string(body2))
	}
}
