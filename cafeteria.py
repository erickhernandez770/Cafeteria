import json
import os


class Cafeteria:
    """Clase para gestionar el menú y las órdenes, ahora con persistencia."""

    def __init__(self, archivo_menu="menu.json"):
        self.archivo_menu = archivo_menu
        self.menu = self._cargar_menu()

        # ------------------------------------

    # MÉTODOS DE MANEJO DE DATOS (Nuevos/Actualizados)
    # ------------------------------------

    def _cargar_menu(self):
        """Método privado para cargar el menú desde el archivo JSON."""
        try:
            with open(self.archivo_menu, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Si el archivo no existe, inicializa con una lista vacía y lo crea.
            print(f"⚠️ Creando archivo '{self.archivo_menu}' vacío.")
            self._guardar_menu([])
            return []
        except json.JSONDecodeError:
            print(f"❌ Error: El archivo '{self.archivo_menu}' no es un JSON válido.")
            return []

    def _guardar_menu(self, menu_data):
        """Método privado para GUARDAR el menú en el archivo JSON."""
        try:
            with open(self.archivo_menu, 'w', encoding='utf-8') as f:
                # Escribe la lista completa de Python al archivo, sobrescribiéndolo.
                json.dump(menu_data, f, indent=4, ensure_ascii=False)
            # print("✔️ Menú guardado con éxito.")
        except Exception as e:
            print(f"❌ Error al guardar el menú: {e}")

    def _obtener_siguiente_id(self):
        """Calcula el siguiente ID único basado en el menú actual."""
        if not self.menu:
            return 1
        # Encuentra el ID más alto y le suma 1
        max_id = max(item['id'] for item in self.menu)
        return max_id + 1

    def agregar_producto(self, nombre, precio, categoria):
        """Agrega un nuevo producto al menú y lo guarda en el JSON."""

        # 1. Crea el nuevo ítem con el ID único
        nuevo_item = {
            "id": self._obtener_siguiente_id(),
            "nombre": nombre,
            "precio": float(precio),  # Asegura que el precio es un float
            "categoria": categoria
        }

        # 2. Agrega el ítem a la lista en memoria
        self.menu.append(nuevo_item)

        # 3. Guarda la lista actualizada en el archivo JSON
        self._guardar_menu(self.menu)

        print(f"\n✨ ¡Producto '{nombre}' agregado con ID: {nuevo_item['id']}! ✨")

    # ------------------------------------
    # MÉTODOS ANTERIORES (Simplificados)
    # ------------------------------------

    def mostrar_menu(self):
        """Muestra el menú disponible."""
        if not self.menu:
            print("El menú no tiene productos. Agrega algunos primero.")
            return

        print("\n☕ Menú de la Cafetería 'El Buen Programador' ☕")
        print("---------------------------------------------")

        categorias = {}
        for item in self.menu:
            categoria = item['categoria']
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(item)

        for categoria, items in categorias.items():
            print(f"\n== {categoria.upper()} ==")
            for item in items:
                print(f"  [{item['id']}] {item['nombre']:<25} ${item['precio']:.2f}")
        print("---------------------------------------------")

    def calcular_total(self, orden):
        """Calcula el costo total de la orden, incluyendo IVA (16%)."""
        subtotal = sum(item['precio'] for item in orden)
        IVA = subtotal * 0.16
        total = subtotal + IVA
        return subtotal, IVA, total

    def tomar_orden(self):
        # (El código de tomar_orden sigue igual, omitido por espacio)
        menu_dict = {item['id']: item for item in self.menu}
        orden = []
        # ... lógica de entrada de datos ...
        return orden  # Retorna la lista de ítems ordenados

    def procesar_pago(self, orden):
        # (El código de procesar_pago sigue igual, omitido por espacio)
        # ... lógica de impresión de recibo ...
        pass  # Simulación de impresión de recibo


# Bloque principal de EJECUCIÓN
if __name__ == "__main__":

    mi_cafeteria = Cafeteria()

    print("\n=============================================")
    print("      GESTOR DE MENÚ Y ÓRDENES DE CAFETERÍA")
    print("=============================================")

    # --- PRUEBA DE AGREGAR PRODUCTOS ---
    print("\n--- 1. AGREGANDO PRODUCTOS ---")

    # Ejemplo de cómo agregar un nuevo producto
    mi_cafeteria.agregar_producto(
        nombre="Tarta de Queso",
        precio=3.75,
        categoria="Postre"
    )

    # Otro ejemplo
    mi_cafeteria.agregar_producto(
        nombre="Smoothie de Mango",
        precio=4.20,
        categoria="Bebida Fría"
    )

    # --- PRUEBA DE VISUALIZACIÓN ---
    print("\n--- 2. MOSTRANDO EL MENÚ ACTUALIZADO ---")
    mi_cafeteria.mostrar_menu()

    # --- PRUEBA DE ORDEN ---
    print("\n--- 3. TOMANDO UNA ORDEN ---")

    # NOTA: Debes descomentar el código de 'tomar_orden' y 'procesar_pago'
    # si quieres la interacción completa, o simular la orden aquí:

    # Simulación de una orden (tomando el último producto agregado, ID 8 y 9 si no has tocado el JSON)
    item_tarta = next((item for item in mi_cafeteria.menu if item['nombre'] == 'Tarta de Queso'), None)
    item_latte = next((item for item in mi_cafeteria.menu if item['nombre'] == 'Latte con Vainilla'), None)

    orden_prueba = []
    if item_tarta: orden_prueba.append(item_tarta)
    if item_latte: orden_prueba.append(item_latte)

    if orden_prueba:
        mi_cafeteria.procesar_pago(orden_prueba)

    print("\n=============================================")