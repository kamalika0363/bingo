import json
import os

import faker_commerce
from dotenv import load_dotenv
from faker import Faker
from supabase import create_client


def add_entries_to_basic_table(supabase, basic_count):
    fake = Faker()
    fake.add_provider(faker_commerce.Provider)
    primary_list = []
    main_list = []
    for i in range(basic_count):
        value = {'category': fake.company(), 'name': fake.name(), 'date': fake.date()}
        main_list.append(value)

    data = supabase.table('Basic').insert(main_list).execute()
    data_json = json.loads(data.json())
    data_entries = data_json['data']

    for i in range(len(data_entries)):
        primary_list.append(int(data_entries[i]['id']))

    return primary_list


def main():
    basic_count = 5
    load_dotenv()
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase = create_client(url, key)
    fk_list = add_entries_to_basic_table(supabase, basic_count)
    for i in range(len(fk_list)):
        add_entries_to_basic_table(supabase, fk_list[i])


main()
