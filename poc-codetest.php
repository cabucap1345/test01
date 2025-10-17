<?php
// Giả lập API login đơn giản với PHP

// Cần cài JWT library: composer require firebase/php-jwt
require __DIR__ . '/vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

// Secret để ký JWT (phải giữ kín)
$jwt_secret = "MY_SUPER_SECRET_KEY";

// Fake DB user
$users = [
    "admin" => "123456",
    "guest" => "guest123"
];

// Hàm login
function login($username, $password, $users, $jwt_secret) {
    if (!isset($users[$username])) {
        return [
            "status" => "error",
            "message" => "User not found"
        ];
    }

    if ($users[$username] !== $password) {
        return [
            "status" => "error",
            "message" => "Invalid password"
        ];
    }

    // Nếu đúng user/pass thì tạo JWT token
    $payload = [
        "iss" => "http://myapi.local", // issuer
        "aud" => "http://myapi.local", // audience
        "iat" => time(),               // issued at
        "exp" => time() + 3600,        // hết hạn sau 1h
        "user" => [
            "username" => $username,
            "role" => $username === "admin" ? "admin" : "user"
        ]
    ];

    $jwt = JWT::encode($payload, $jwt_secret, 'HS256');

    return [
        "status" => "success",
        "access_token" => $jwt,
        "token_type" => "Bearer",
        "expires_in" => 3600
    ];
}

// ============================
// Demo login
// ============================
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents("php://input"), true);
    $username = $data["username"] ?? "";
    $password = $data["password"] ?? "";

    $result = login($username, $password, $users, $jwt_secret);

    header('Content-Type: application/json');
    echo json_encode($result);
} else {
    echo "Please POST username & password as JSON.";
}
