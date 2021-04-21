from dbcon import openConnection, closeConnection

def doQuery() :
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( "SELECT * FROM processor" )

    for processor in cur.fetchall() :
        for val in processor:
            print(val)
    closeConnection(connection)

def insertProcessor(processor):
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( f"INSERT INTO processor VALUES (DEFAULT, '{str(processor.name)}', '{str(processor.series)}', '{int(processor.cores)}', '{str(processor.core_clock)}', '{str(processor.boost_clock)}', '{str(processor.socket)}', '{str(processor.integrated_graphics)}', '{str(processor.includes_cooler)}', '{str(processor.cache_memory)}', '{str(processor.image)}') RETURNING id;")
    id_of_new_row = cur.fetchone()[0]
    cur.execute( f"INSERT INTO offer VALUES (DEFAULT, '{str(processor.offer.shop)}', '{str(processor.offer.link)}', '{int(processor.offer.original_price)}', '{int(processor.offer.current_price)}', '{int(id_of_new_row)}')")
    connection.commit()
    closeConnection(connection)

def insertMotherboard(motherboard):
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( f"INSERT INTO motherboard VALUES (DEFAULT, '{str(motherboard.name)}', '{str(motherboard.socket)}', '{str(motherboard.chipset)}', '{str(motherboard.memory_slots)}', '{str(motherboard.memory_speed)}', '{str(motherboard.memory_max)}', '{str(motherboard.format)}', '{str(motherboard.image)}') RETURNING id;")
    id_of_new_row = cur.fetchone()[0]
    cur.execute( f"INSERT INTO offer VALUES (DEFAULT, '{str(motherboard.offer.shop)}', '{str(motherboard.offer.link)}', '{int(motherboard.offer.original_price)}', '{int(motherboard.offer.current_price)}', NULL, '{int(id_of_new_row)}')")
    connection.commit()
    closeConnection(connection)

def insertGPU(gpu):
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( f"INSERT INTO gpu VALUES (DEFAULT, '{str(gpu.name)}', '{str(gpu.chipset)}', '{str(gpu.memory)}', '{str(gpu.core_clock)}', '{str(gpu.boost_clock)}', '{str(gpu.image)}') RETURNING id;")
    id_of_new_row = cur.fetchone()[0]
    cur.execute( f"INSERT INTO offer VALUES (DEFAULT, '{str(gpu.offer.shop)}', '{str(gpu.offer.link)}', '{int(gpu.offer.original_price)}', '{int(gpu.offer.current_price)}', NULL, NULL, '{int(id_of_new_row)}')")
    connection.commit()
    closeConnection(connection)

def inserCPUCooler(cpu_cooler):
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( f"INSERT INTO cpu_cooler VALUES (DEFAULT, '{str(cpu_cooler.name)}', '{str(cpu_cooler.rpm)}', '{str(cpu_cooler.noise)}', '{str(cpu_cooler.compatibility)}', '{str(cpu_cooler.image)}') RETURNING id;")
    id_of_new_row = cur.fetchone()[0]
    cur.execute( f"INSERT INTO offer VALUES (DEFAULT, '{str(cpu_cooler.offer.shop)}', '{str(cpu_cooler.offer.link)}', '{int(cpu_cooler.offer.original_price)}', '{int(cpu_cooler.offer.current_price)}', NULL, NULL, NULL, '{int(id_of_new_row)}')")
    connection.commit()
    closeConnection(connection)

def insertCase(case):
    connection = openConnection()
    cur = connection.cursor()
    cur.execute( f"INSERT INTO pc_case VALUES (DEFAULT, '{str(case.name)}', '{str(case.cabinet_type)}', '{str(case.side_panel)}', '{str(case.image)}') RETURNING id;")
    id_of_new_row = cur.fetchone()[0]
    cur.execute( f"INSERT INTO offer VALUES (DEFAULT, '{str(case.offer.shop)}', '{str(case.offer.link)}', '{int(case.offer.original_price)}', '{int(case.offer.current_price)}', NULL, NULL, NULL, NULL, '{int(id_of_new_row)}')")
    connection.commit()
    closeConnection(connection)