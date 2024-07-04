# Функция для расчета от количества акций
def calculate_from_shares():
    kolichestvo_aktsii = int(input("Введите количество акций (целое число): "))
    sub_fee_percentage = float(input("Введите процент Sub Fee (например, 5 для 5%): ").replace(',', '.')) / 100
    tsena_aktsii = float(input("Введите цену акции: ").replace(',', '.'))

    # Шаг 1: Вычисляем общую стоимость акций без учета Sub Fee
    stoimost_aktsii = kolichestvo_aktsii * tsena_aktsii

    # Шаг 2: Вычисляем общую стоимость с учетом Sub Fee
    obshaya_stoimost = stoimost_aktsii * (1 + sub_fee_percentage)

    # Шаг 3: Округляем общую стоимость до целого числа
    denezhnie_sredstva = round(obshaya_stoimost)

    # Шаг 4: Пересчитываем Sub Fee фонда на основе округленной суммы
    sub_fee_fonda_okrugl = (denezhnie_sredstva * sub_fee_percentage) / (1 + sub_fee_percentage)

    # Шаг 5: Вычисляем остаток средств
    ostatok_sredstv = denezhnie_sredstva - stoimost_aktsii - sub_fee_fonda_okrugl

    # Шаг 6: Складываем необходимый остаток средств, Sub Fee на основе округленной суммы и стоимость акций без учета Sub Fee
    neobhodimaya_summa = round(abs(ostatok_sredstv) + sub_fee_fonda_okrugl + stoimost_aktsii)

    # Шаг 7: Вычисляем остаток у клиента
    ostatok_u_klienta = neobhodimaya_summa - stoimost_aktsii - sub_fee_fonda_okrugl

    # Вывод результатов
    print(f"Стоимость акций: {stoimost_aktsii:.2f}")
    print(f"Sub Fee фонда: {sub_fee_fonda_okrugl:.2f}")
    print(f"Необходимая сумма денежных средств: {denezhnie_sredstva}")
    print(f"Остаток средств: {ostatok_sredstv:.2f}")
    print(f"Необходимая сумма с учетом остатка: {neobhodimaya_summa}")
    print(f"Остаток у клиента: {ostatok_u_klienta:.2f}")

# Функция для расчета от суммы денежных средств
def calculate_from_amount():
    denezhnie_sredstva = float(input("Введите сумму денежных средств: ").replace(',', '.'))
    sub_fee_percentage = float(input("Введите процент Sub Fee (например, 5 для 5%): ").replace(',', '.')) / 100
    tsena_aktsii = float(input("Введите цену акции: ").replace(',', '.'))

    # Шаг 1: Вычисляем сумму покупки без учета Sub Fee
    summa_pokupki = denezhnie_sredstva / (1 + sub_fee_percentage)

    # Шаг 2: Вычисляем количество акций
    kolichestvo_aktsii = int(summa_pokupki // tsena_aktsii)

    # Шаг 3: Вычисляем Sub Fee фонда
    sub_fee_fonda = kolichestvo_aktsii * tsena_aktsii * sub_fee_percentage

    # Шаг 4: Вычисляем остаток средств
    ostatok_sredstv = denezhnie_sredstva - (kolichestvo_aktsii * tsena_aktsii) - sub_fee_fonda

    # Вывод результатов
    print(f"Количество акций: {kolichestvo_aktsii}")
    print(f"Sub Fee фонда: {sub_fee_fonda:.2f}")
    print(f"Остаток средств: {ostatok_sredstv:.2f}")

# Основной код
choice = input("Вам нужно рассчитать от суммы или от количества акций? Введите '1' для суммы или '2' для акций: ").strip()

if choice == '2':
    calculate_from_shares()
elif choice == '1':
    calculate_from_amount()
else:
    print("Неправильный ввод. Пожалуйста, введите '1' или '2'.")
