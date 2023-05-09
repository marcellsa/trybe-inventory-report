from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "CADEIRA",
        "Forces of Nature",
        "2022-04-04",
        "2023-02-09",
        "FR48",
        "Conservar em local fresco",
    )
    assert produto.id == 1
    assert produto.nome_da_empresa == "Forces of Nature"
    assert produto.data_de_fabricacao == "2022-04-04"
    assert produto.data_de_validade == "2023-02-09"
    assert produto.numero_de_serie == "FR48"
    assert produto.instrucoes_de_armazenamento == "Conservar em local fresco"
