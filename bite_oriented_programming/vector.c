#include <stdio.h>
#include <stdlib.h>

typedef struct {
    float x, y, z;
} Vector;

typedef struct {
    int r, g, b, a;
} Color;

typedef struct {
    Vector position;
    Color color;
} Vertex;

int main() {
    FILE *file = fopen("data.bin", "wb");
    if (!file) {
        perror("Nie udało się otworzyć pliku");
        return 1;
    }

    // Przykładowe dane
    Vertex vertices[3] = {
        {{1.0f, 2.0f, 3.0f}, {255, 0, 0, 255}},  // czerwony
        {{4.0f, 5.0f, 6.0f}, {0, 255, 0, 255}},  // zielony
        {{7.0f, 8.0f, 9.0f}, {0, 0, 255, 255}}   // niebieski
    };

    fwrite(vertices, sizeof(Vertex), 3, file);
    fclose(file);

    printf("Dane zapisane do pliku binarnego.\n");
    return 0;
}