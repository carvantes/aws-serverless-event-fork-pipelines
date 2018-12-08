import pytest
import process_records


def test_handler(mocker):
    mocker.patch.object(process_records, 'TABLE')
    event = {
        'Records': [
            {
                'id': 1,
                'date': '2018-12-15T23:41:11-08:00',
                'status': 'confirmed',
                'customer': {
                    'id': 100
                }
            },
            {
                'id': 2,
                'date': '2018-12-16T23:41:11-08:00',
                'status': 'confirmed',
                'customer': {
                    'id': 101
                }
            }
        ]
    }
    process_records.handler(event, None)
    process_records.TABLE.put_item.assert_called()
    assert process_records.TABLE.put_item.call_count == 2


def test_handler_no_records(mocker):
    mocker.patch.object(process_records, 'TABLE')
    process_records.handler({}, None)
    process_records.TABLE.put_item.assert_not_called()