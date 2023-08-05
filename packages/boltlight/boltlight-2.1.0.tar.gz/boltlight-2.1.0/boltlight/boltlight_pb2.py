# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: boltlight/boltlight.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x62oltlight/boltlight.proto\x12\tboltlight\"6\n\rUnlockRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x13\n\x0bunlock_node\x18\x02 \x01(\x08\"\'\n\x0eUnlockResponse\x12\x15\n\rnode_unlocked\x18\x01 \x01(\x08\"\x10\n\x0eGetInfoRequest\"U\n\x0fGetInfoResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1b\n\x13node_implementation\x18\x02 \x01(\t\x12\x14\n\x0cnode_version\x18\x03 \x01(\t\"\r\n\x0bLockRequest\"\x0e\n\x0cLockResponse\"\x18\n\x16\x42\x61lanceOffChainRequest\"w\n\x17\x42\x61lanceOffChainResponse\x12\x14\n\x0cout_tot_msat\x18\x01 \x01(\x04\x12\x18\n\x10out_tot_now_msat\x18\x02 \x01(\x04\x12\x13\n\x0bin_tot_msat\x18\x04 \x01(\x04\x12\x17\n\x0fin_tot_now_msat\x18\x05 \x01(\x04\"+\n\x13\x43heckInvoiceRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\t\"?\n\x14\x43heckInvoiceResponse\x12\'\n\x05state\x18\x01 \x01(\x0e\x32\x18.boltlight.Invoice.State\"8\n\x13\x43loseChannelRequest\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\",\n\x14\x43loseChannelResponse\x12\x14\n\x0c\x63losing_txid\x18\x01 \x01(\t\"\x86\x01\n\x14\x43reateInvoiceRequest\x12\x13\n\x0b\x61mount_msat\x18\x01 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06\x65xpiry\x18\x03 \x01(\r\x12\x1d\n\x15min_final_cltv_expiry\x18\x04 \x01(\r\x12\x15\n\rfallback_addr\x18\x05 \x01(\t\"Z\n\x15\x43reateInvoiceResponse\x12\x17\n\x0fpayment_request\x18\x01 \x01(\t\x12\x14\n\x0cpayment_hash\x18\x02 \x01(\t\x12\x12\n\nexpires_at\x18\x03 \x01(\x04\"\x14\n\x12GetNodeInfoRequest\"D\n\x14\x44\x65\x63odeInvoiceRequest\x12\x17\n\x0fpayment_request\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x91\x02\n\x15\x44\x65\x63odeInvoiceResponse\x12\x13\n\x0b\x61mount_msat\x18\x01 \x01(\x04\x12\x14\n\x0cpayment_hash\x18\x02 \x01(\t\x12\x1a\n\x12\x64\x65stination_pubkey\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x18\n\x10\x64\x65scription_hash\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x0e\n\x06\x65xpiry\x18\x07 \x01(\r\x12\x1d\n\x15min_final_cltv_expiry\x18\x08 \x01(\r\x12\x15\n\rfallback_addr\x18\t \x01(\t\x12)\n\x0broute_hints\x18\n \x03(\x0b\x32\x14.boltlight.RouteHint\"2\n\tRouteHint\x12%\n\thop_hints\x18\x01 \x03(\x0b\x32\x12.boltlight.HopHint\"\x8a\x01\n\x07HopHint\x12\x0e\n\x06pubkey\x18\x01 \x01(\t\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x15\n\rfee_base_msat\x18\x03 \x01(\r\x12#\n\x1b\x66\x65\x65_proportional_millionths\x18\x04 \x01(\r\x12\x19\n\x11\x63ltv_expiry_delta\x18\x05 \x01(\r\"E\n\x07Network\":\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07MAINNET\x10\x01\x12\x0b\n\x07TESTNET\x10\x02\x12\x0b\n\x07REGTEST\x10\x03\"\x9e\x01\n\x13GetNodeInfoResponse\x12\x10\n\x08node_uri\x18\x01 \x01(\t\x12\x17\n\x0fidentity_pubkey\x18\x02 \x01(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\x12\x14\n\x0c\x62lock_height\x18\x05 \x01(\r\x12(\n\x07network\x18\x06 \x01(\x0e\x32\x17.boltlight.Network.Name\"*\n\x13ListChannelsRequest\x12\x13\n\x0b\x61\x63tive_only\x18\x01 \x01(\x08\"<\n\x14ListChannelsResponse\x12$\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x12.boltlight.Channel\"\xb1\x03\n\x07\x43hannel\x12\x15\n\rremote_pubkey\x18\x01 \x01(\t\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0c\x66unding_txid\x18\x04 \x01(\t\x12\x15\n\rcapacity_msat\x18\x05 \x01(\x04\x12\x1a\n\x12local_balance_msat\x18\x06 \x01(\x04\x12\x1b\n\x13remote_balance_msat\x18\x07 \x01(\x04\x12\x19\n\x11local_reserve_sat\x18\x08 \x01(\x04\x12\x1a\n\x12remote_reserve_sat\x18\t \x01(\x04\x12\x15\n\rto_self_delay\x18\n \x01(\r\x12\x0f\n\x07private\x18\x0b \x01(\x08\x12\'\n\x05state\x18\x0c \x01(\x0e\x32\x18.boltlight.Channel.State\x12\x0e\n\x06\x61\x63tive\x18\r \x01(\x08\"c\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cPENDING_OPEN\x10\x01\x12\x08\n\x04OPEN\x10\x02\x12\x18\n\x14PENDING_MUTUAL_CLOSE\x10\x03\x12\x17\n\x13PENDING_FORCE_CLOSE\x10\x04\"\xe5\x01\n\x13ListInvoicesRequest\x12\x11\n\tmax_items\x18\x01 \x01(\r\x12\x18\n\x10search_timestamp\x18\x02 \x01(\x04\x12\x30\n\x0csearch_order\x18\x03 \x01(\x0e\x32\x1a.boltlight.Order.Direction\x12.\n\nlist_order\x18\x04 \x01(\x0e\x32\x1a.boltlight.Order.Direction\x12\x0c\n\x04paid\x18\x05 \x01(\x08\x12\x0f\n\x07pending\x18\x06 \x01(\x08\x12\x0f\n\x07\x65xpired\x18\x07 \x01(\x08\x12\x0f\n\x07unknown\x18\x08 \x01(\x08\"<\n\x14ListInvoicesResponse\x12$\n\x08invoices\x18\x01 \x03(\x0b\x32\x12.boltlight.Invoice\"3\n\x05Order\"*\n\tDirection\x12\r\n\tASCENDING\x10\x00\x12\x0e\n\nDESCENDING\x10\x01\"\xea\x02\n\x07Invoice\x12\x1b\n\x13\x61mount_encoded_msat\x18\x01 \x01(\x04\x12\x1c\n\x14\x61mount_received_msat\x18\x02 \x01(\x04\x12\x14\n\x0cpayment_hash\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x18\n\x10\x64\x65scription_hash\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x0e\n\x06\x65xpiry\x18\x07 \x01(\r\x12\x15\n\rfallback_addr\x18\x08 \x01(\t\x12)\n\x0broute_hints\x18\t \x03(\x0b\x32\x14.boltlight.RouteHint\x12\'\n\x05state\x18\n \x01(\x0e\x32\x18.boltlight.Invoice.State\x12\x17\n\x0fpayment_request\x18\x0b \x01(\t\"8\n\x05State\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04PAID\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07\x45XPIRED\x10\x03\"\x15\n\x13ListPaymentsRequest\"<\n\x14ListPaymentsResponse\x12$\n\x08payments\x18\x01 \x03(\x0b\x32\x12.boltlight.Payment\"s\n\x07Payment\x12\x13\n\x0b\x61mount_msat\x18\x01 \x01(\x04\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12\x14\n\x0cpayment_hash\x18\x03 \x01(\t\x12\x18\n\x10payment_preimage\x18\x04 \x01(\t\x12\x10\n\x08\x66\x65\x65_msat\x18\x05 \x01(\x04\"\x12\n\x10ListPeersRequest\"3\n\x11ListPeersResponse\x12\x1e\n\x05peers\x18\x01 \x03(\x0b\x32\x0f.boltlight.Peer\"E\n\x04Peer\x12\x0e\n\x06pubkey\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\t\"\x19\n\x17ListTransactionsRequest\"H\n\x18ListTransactionsResponse\x12,\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x16.boltlight.Transaction\"\x94\x01\n\x0bTransaction\x12\x12\n\namount_sat\x18\x01 \x01(\x03\x12\x0c\n\x04txid\x18\x02 \x01(\t\x12\x15\n\rconfirmations\x18\x03 \x01(\r\x12\x14\n\x0c\x62lock_height\x18\x04 \x01(\r\x12\x12\n\nblock_hash\x18\x05 \x01(\t\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x12\x0f\n\x07\x66\x65\x65_sat\x18\x07 \x01(\x04\"?\n\x11NewAddressRequest\x12*\n\taddr_type\x18\x01 \x01(\x0e\x32\x17.boltlight.Address.Type\"%\n\x12NewAddressResponse\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"T\n\x07\x41\x64\x64ress\"I\n\x04Type\x12\n\n\x06P2WPKH\x10\x00\x12\x11\n\rNATIVE_SEGWIT\x10\x00\x12\x0b\n\x07NP2WPKH\x10\x01\x12\x11\n\rNESTED_SEGWIT\x10\x01\x1a\x02\x10\x01\"_\n\x12OpenChannelRequest\x12\x10\n\x08node_uri\x18\x01 \x01(\t\x12\x13\n\x0b\x66unding_sat\x18\x02 \x01(\x04\x12\x11\n\tpush_msat\x18\x03 \x01(\x04\x12\x0f\n\x07private\x18\x04 \x01(\x08\"+\n\x13OpenChannelResponse\x12\x14\n\x0c\x66unding_txid\x18\x01 \x01(\t\"q\n\x11PayInvoiceRequest\x12\x17\n\x0fpayment_request\x18\x01 \x01(\t\x12\x13\n\x0b\x61mount_msat\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x19\n\x11\x63ltv_expiry_delta\x18\x04 \x01(\r\".\n\x12PayInvoiceResponse\x12\x18\n\x10payment_preimage\x18\x01 \x01(\t\"N\n\x11PayOnChainRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\namount_sat\x18\x02 \x01(\x04\x12\x14\n\x0c\x66\x65\x65_sat_byte\x18\x03 \x01(\r\"\"\n\x12PayOnChainResponse\x12\x0c\n\x04txid\x18\x01 \x01(\t\"%\n\x11UnlockNodeRequest\x12\x10\n\x08password\x18\x01 \x01(\t\"\x14\n\x12UnlockNodeResponse\"\x17\n\x15\x42\x61lanceOnChainRequest\"B\n\x16\x42\x61lanceOnChainResponse\x12\x15\n\rconfirmed_sat\x18\x01 \x01(\x04\x12\x11\n\ttotal_sat\x18\x02 \x01(\x04\x32I\n\x08Unlocker\x12=\n\x06Unlock\x12\x18.boltlight.UnlockRequest\x1a\x19.boltlight.UnlockResponse2\x86\x01\n\tBoltlight\x12@\n\x07GetInfo\x12\x19.boltlight.GetInfoRequest\x1a\x1a.boltlight.GetInfoResponse\x12\x37\n\x04Lock\x12\x16.boltlight.LockRequest\x1a\x17.boltlight.LockResponse2\xe6\n\n\tLightning\x12X\n\x0f\x42\x61lanceOffChain\x12!.boltlight.BalanceOffChainRequest\x1a\".boltlight.BalanceOffChainResponse\x12U\n\x0e\x42\x61lanceOnChain\x12 .boltlight.BalanceOnChainRequest\x1a!.boltlight.BalanceOnChainResponse\x12O\n\x0c\x43heckInvoice\x12\x1e.boltlight.CheckInvoiceRequest\x1a\x1f.boltlight.CheckInvoiceResponse\x12O\n\x0c\x43loseChannel\x12\x1e.boltlight.CloseChannelRequest\x1a\x1f.boltlight.CloseChannelResponse\x12R\n\rCreateInvoice\x12\x1f.boltlight.CreateInvoiceRequest\x1a .boltlight.CreateInvoiceResponse\x12R\n\rDecodeInvoice\x12\x1f.boltlight.DecodeInvoiceRequest\x1a .boltlight.DecodeInvoiceResponse\x12L\n\x0bGetNodeInfo\x12\x1d.boltlight.GetNodeInfoRequest\x1a\x1e.boltlight.GetNodeInfoResponse\x12O\n\x0cListChannels\x12\x1e.boltlight.ListChannelsRequest\x1a\x1f.boltlight.ListChannelsResponse\x12O\n\x0cListInvoices\x12\x1e.boltlight.ListInvoicesRequest\x1a\x1f.boltlight.ListInvoicesResponse\x12O\n\x0cListPayments\x12\x1e.boltlight.ListPaymentsRequest\x1a\x1f.boltlight.ListPaymentsResponse\x12\x46\n\tListPeers\x12\x1b.boltlight.ListPeersRequest\x1a\x1c.boltlight.ListPeersResponse\x12[\n\x10ListTransactions\x12\".boltlight.ListTransactionsRequest\x1a#.boltlight.ListTransactionsResponse\x12I\n\nNewAddress\x12\x1c.boltlight.NewAddressRequest\x1a\x1d.boltlight.NewAddressResponse\x12L\n\x0bOpenChannel\x12\x1d.boltlight.OpenChannelRequest\x1a\x1e.boltlight.OpenChannelResponse\x12I\n\nPayInvoice\x12\x1c.boltlight.PayInvoiceRequest\x1a\x1d.boltlight.PayInvoiceResponse\x12I\n\nPayOnChain\x12\x1c.boltlight.PayOnChainRequest\x1a\x1d.boltlight.PayOnChainResponse\x12I\n\nUnlockNode\x12\x1c.boltlight.UnlockNodeRequest\x1a\x1d.boltlight.UnlockNodeResponseb\x06proto3')



_UNLOCKREQUEST = DESCRIPTOR.message_types_by_name['UnlockRequest']
_UNLOCKRESPONSE = DESCRIPTOR.message_types_by_name['UnlockResponse']
_GETINFOREQUEST = DESCRIPTOR.message_types_by_name['GetInfoRequest']
_GETINFORESPONSE = DESCRIPTOR.message_types_by_name['GetInfoResponse']
_LOCKREQUEST = DESCRIPTOR.message_types_by_name['LockRequest']
_LOCKRESPONSE = DESCRIPTOR.message_types_by_name['LockResponse']
_BALANCEOFFCHAINREQUEST = DESCRIPTOR.message_types_by_name['BalanceOffChainRequest']
_BALANCEOFFCHAINRESPONSE = DESCRIPTOR.message_types_by_name['BalanceOffChainResponse']
_CHECKINVOICEREQUEST = DESCRIPTOR.message_types_by_name['CheckInvoiceRequest']
_CHECKINVOICERESPONSE = DESCRIPTOR.message_types_by_name['CheckInvoiceResponse']
_CLOSECHANNELREQUEST = DESCRIPTOR.message_types_by_name['CloseChannelRequest']
_CLOSECHANNELRESPONSE = DESCRIPTOR.message_types_by_name['CloseChannelResponse']
_CREATEINVOICEREQUEST = DESCRIPTOR.message_types_by_name['CreateInvoiceRequest']
_CREATEINVOICERESPONSE = DESCRIPTOR.message_types_by_name['CreateInvoiceResponse']
_GETNODEINFOREQUEST = DESCRIPTOR.message_types_by_name['GetNodeInfoRequest']
_DECODEINVOICEREQUEST = DESCRIPTOR.message_types_by_name['DecodeInvoiceRequest']
_DECODEINVOICERESPONSE = DESCRIPTOR.message_types_by_name['DecodeInvoiceResponse']
_ROUTEHINT = DESCRIPTOR.message_types_by_name['RouteHint']
_HOPHINT = DESCRIPTOR.message_types_by_name['HopHint']
_NETWORK = DESCRIPTOR.message_types_by_name['Network']
_GETNODEINFORESPONSE = DESCRIPTOR.message_types_by_name['GetNodeInfoResponse']
_LISTCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['ListChannelsRequest']
_LISTCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['ListChannelsResponse']
_CHANNEL = DESCRIPTOR.message_types_by_name['Channel']
_LISTINVOICESREQUEST = DESCRIPTOR.message_types_by_name['ListInvoicesRequest']
_LISTINVOICESRESPONSE = DESCRIPTOR.message_types_by_name['ListInvoicesResponse']
_ORDER = DESCRIPTOR.message_types_by_name['Order']
_INVOICE = DESCRIPTOR.message_types_by_name['Invoice']
_LISTPAYMENTSREQUEST = DESCRIPTOR.message_types_by_name['ListPaymentsRequest']
_LISTPAYMENTSRESPONSE = DESCRIPTOR.message_types_by_name['ListPaymentsResponse']
_PAYMENT = DESCRIPTOR.message_types_by_name['Payment']
_LISTPEERSREQUEST = DESCRIPTOR.message_types_by_name['ListPeersRequest']
_LISTPEERSRESPONSE = DESCRIPTOR.message_types_by_name['ListPeersResponse']
_PEER = DESCRIPTOR.message_types_by_name['Peer']
_LISTTRANSACTIONSREQUEST = DESCRIPTOR.message_types_by_name['ListTransactionsRequest']
_LISTTRANSACTIONSRESPONSE = DESCRIPTOR.message_types_by_name['ListTransactionsResponse']
_TRANSACTION = DESCRIPTOR.message_types_by_name['Transaction']
_NEWADDRESSREQUEST = DESCRIPTOR.message_types_by_name['NewAddressRequest']
_NEWADDRESSRESPONSE = DESCRIPTOR.message_types_by_name['NewAddressResponse']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_OPENCHANNELREQUEST = DESCRIPTOR.message_types_by_name['OpenChannelRequest']
_OPENCHANNELRESPONSE = DESCRIPTOR.message_types_by_name['OpenChannelResponse']
_PAYINVOICEREQUEST = DESCRIPTOR.message_types_by_name['PayInvoiceRequest']
_PAYINVOICERESPONSE = DESCRIPTOR.message_types_by_name['PayInvoiceResponse']
_PAYONCHAINREQUEST = DESCRIPTOR.message_types_by_name['PayOnChainRequest']
_PAYONCHAINRESPONSE = DESCRIPTOR.message_types_by_name['PayOnChainResponse']
_UNLOCKNODEREQUEST = DESCRIPTOR.message_types_by_name['UnlockNodeRequest']
_UNLOCKNODERESPONSE = DESCRIPTOR.message_types_by_name['UnlockNodeResponse']
_BALANCEONCHAINREQUEST = DESCRIPTOR.message_types_by_name['BalanceOnChainRequest']
_BALANCEONCHAINRESPONSE = DESCRIPTOR.message_types_by_name['BalanceOnChainResponse']
_NETWORK_NAME = _NETWORK.enum_types_by_name['Name']
_CHANNEL_STATE = _CHANNEL.enum_types_by_name['State']
_ORDER_DIRECTION = _ORDER.enum_types_by_name['Direction']
_INVOICE_STATE = _INVOICE.enum_types_by_name['State']
_ADDRESS_TYPE = _ADDRESS.enum_types_by_name['Type']
UnlockRequest = _reflection.GeneratedProtocolMessageType('UnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.UnlockRequest)
  })
_sym_db.RegisterMessage(UnlockRequest)

UnlockResponse = _reflection.GeneratedProtocolMessageType('UnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.UnlockResponse)
  })
_sym_db.RegisterMessage(UnlockResponse)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)

LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

LockResponse = _reflection.GeneratedProtocolMessageType('LockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOCKRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.LockResponse)
  })
_sym_db.RegisterMessage(LockResponse)

BalanceOffChainRequest = _reflection.GeneratedProtocolMessageType('BalanceOffChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEOFFCHAINREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.BalanceOffChainRequest)
  })
_sym_db.RegisterMessage(BalanceOffChainRequest)

BalanceOffChainResponse = _reflection.GeneratedProtocolMessageType('BalanceOffChainResponse', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEOFFCHAINRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.BalanceOffChainResponse)
  })
_sym_db.RegisterMessage(BalanceOffChainResponse)

CheckInvoiceRequest = _reflection.GeneratedProtocolMessageType('CheckInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINVOICEREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CheckInvoiceRequest)
  })
_sym_db.RegisterMessage(CheckInvoiceRequest)

CheckInvoiceResponse = _reflection.GeneratedProtocolMessageType('CheckInvoiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKINVOICERESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CheckInvoiceResponse)
  })
_sym_db.RegisterMessage(CheckInvoiceResponse)

CloseChannelRequest = _reflection.GeneratedProtocolMessageType('CloseChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLOSECHANNELREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CloseChannelRequest)
  })
_sym_db.RegisterMessage(CloseChannelRequest)

CloseChannelResponse = _reflection.GeneratedProtocolMessageType('CloseChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLOSECHANNELRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CloseChannelResponse)
  })
_sym_db.RegisterMessage(CloseChannelResponse)

CreateInvoiceRequest = _reflection.GeneratedProtocolMessageType('CreateInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINVOICEREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CreateInvoiceRequest)
  })
_sym_db.RegisterMessage(CreateInvoiceRequest)

CreateInvoiceResponse = _reflection.GeneratedProtocolMessageType('CreateInvoiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEINVOICERESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.CreateInvoiceResponse)
  })
_sym_db.RegisterMessage(CreateInvoiceResponse)

GetNodeInfoRequest = _reflection.GeneratedProtocolMessageType('GetNodeInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNODEINFOREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.GetNodeInfoRequest)
  })
_sym_db.RegisterMessage(GetNodeInfoRequest)

DecodeInvoiceRequest = _reflection.GeneratedProtocolMessageType('DecodeInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECODEINVOICEREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.DecodeInvoiceRequest)
  })
_sym_db.RegisterMessage(DecodeInvoiceRequest)

DecodeInvoiceResponse = _reflection.GeneratedProtocolMessageType('DecodeInvoiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECODEINVOICERESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.DecodeInvoiceResponse)
  })
_sym_db.RegisterMessage(DecodeInvoiceResponse)

RouteHint = _reflection.GeneratedProtocolMessageType('RouteHint', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHINT,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.RouteHint)
  })
_sym_db.RegisterMessage(RouteHint)

HopHint = _reflection.GeneratedProtocolMessageType('HopHint', (_message.Message,), {
  'DESCRIPTOR' : _HOPHINT,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.HopHint)
  })
_sym_db.RegisterMessage(HopHint)

Network = _reflection.GeneratedProtocolMessageType('Network', (_message.Message,), {
  'DESCRIPTOR' : _NETWORK,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Network)
  })
_sym_db.RegisterMessage(Network)

GetNodeInfoResponse = _reflection.GeneratedProtocolMessageType('GetNodeInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETNODEINFORESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.GetNodeInfoResponse)
  })
_sym_db.RegisterMessage(GetNodeInfoResponse)

ListChannelsRequest = _reflection.GeneratedProtocolMessageType('ListChannelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTCHANNELSREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListChannelsRequest)
  })
_sym_db.RegisterMessage(ListChannelsRequest)

ListChannelsResponse = _reflection.GeneratedProtocolMessageType('ListChannelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTCHANNELSRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListChannelsResponse)
  })
_sym_db.RegisterMessage(ListChannelsResponse)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Channel)
  })
_sym_db.RegisterMessage(Channel)

ListInvoicesRequest = _reflection.GeneratedProtocolMessageType('ListInvoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListInvoicesRequest)
  })
_sym_db.RegisterMessage(ListInvoicesRequest)

ListInvoicesResponse = _reflection.GeneratedProtocolMessageType('ListInvoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTINVOICESRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListInvoicesResponse)
  })
_sym_db.RegisterMessage(ListInvoicesResponse)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Order)
  })
_sym_db.RegisterMessage(Order)

Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), {
  'DESCRIPTOR' : _INVOICE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Invoice)
  })
_sym_db.RegisterMessage(Invoice)

ListPaymentsRequest = _reflection.GeneratedProtocolMessageType('ListPaymentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListPaymentsRequest)
  })
_sym_db.RegisterMessage(ListPaymentsRequest)

ListPaymentsResponse = _reflection.GeneratedProtocolMessageType('ListPaymentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListPaymentsResponse)
  })
_sym_db.RegisterMessage(ListPaymentsResponse)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENT,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Payment)
  })
_sym_db.RegisterMessage(Payment)

ListPeersRequest = _reflection.GeneratedProtocolMessageType('ListPeersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERSREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListPeersRequest)
  })
_sym_db.RegisterMessage(ListPeersRequest)

ListPeersResponse = _reflection.GeneratedProtocolMessageType('ListPeersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERSRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListPeersResponse)
  })
_sym_db.RegisterMessage(ListPeersResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Peer)
  })
_sym_db.RegisterMessage(Peer)

ListTransactionsRequest = _reflection.GeneratedProtocolMessageType('ListTransactionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSACTIONSREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListTransactionsRequest)
  })
_sym_db.RegisterMessage(ListTransactionsRequest)

ListTransactionsResponse = _reflection.GeneratedProtocolMessageType('ListTransactionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRANSACTIONSRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.ListTransactionsResponse)
  })
_sym_db.RegisterMessage(ListTransactionsResponse)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Transaction)
  })
_sym_db.RegisterMessage(Transaction)

NewAddressRequest = _reflection.GeneratedProtocolMessageType('NewAddressRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRESSREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.NewAddressRequest)
  })
_sym_db.RegisterMessage(NewAddressRequest)

NewAddressResponse = _reflection.GeneratedProtocolMessageType('NewAddressResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWADDRESSRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.NewAddressResponse)
  })
_sym_db.RegisterMessage(NewAddressResponse)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.Address)
  })
_sym_db.RegisterMessage(Address)

OpenChannelRequest = _reflection.GeneratedProtocolMessageType('OpenChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENCHANNELREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.OpenChannelRequest)
  })
_sym_db.RegisterMessage(OpenChannelRequest)

OpenChannelResponse = _reflection.GeneratedProtocolMessageType('OpenChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENCHANNELRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.OpenChannelResponse)
  })
_sym_db.RegisterMessage(OpenChannelResponse)

PayInvoiceRequest = _reflection.GeneratedProtocolMessageType('PayInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAYINVOICEREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.PayInvoiceRequest)
  })
_sym_db.RegisterMessage(PayInvoiceRequest)

PayInvoiceResponse = _reflection.GeneratedProtocolMessageType('PayInvoiceResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAYINVOICERESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.PayInvoiceResponse)
  })
_sym_db.RegisterMessage(PayInvoiceResponse)

PayOnChainRequest = _reflection.GeneratedProtocolMessageType('PayOnChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAYONCHAINREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.PayOnChainRequest)
  })
_sym_db.RegisterMessage(PayOnChainRequest)

PayOnChainResponse = _reflection.GeneratedProtocolMessageType('PayOnChainResponse', (_message.Message,), {
  'DESCRIPTOR' : _PAYONCHAINRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.PayOnChainResponse)
  })
_sym_db.RegisterMessage(PayOnChainResponse)

UnlockNodeRequest = _reflection.GeneratedProtocolMessageType('UnlockNodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKNODEREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.UnlockNodeRequest)
  })
_sym_db.RegisterMessage(UnlockNodeRequest)

UnlockNodeResponse = _reflection.GeneratedProtocolMessageType('UnlockNodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKNODERESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.UnlockNodeResponse)
  })
_sym_db.RegisterMessage(UnlockNodeResponse)

BalanceOnChainRequest = _reflection.GeneratedProtocolMessageType('BalanceOnChainRequest', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEONCHAINREQUEST,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.BalanceOnChainRequest)
  })
_sym_db.RegisterMessage(BalanceOnChainRequest)

BalanceOnChainResponse = _reflection.GeneratedProtocolMessageType('BalanceOnChainResponse', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEONCHAINRESPONSE,
  '__module__' : 'boltlight.boltlight_pb2'
  # @@protoc_insertion_point(class_scope:boltlight.BalanceOnChainResponse)
  })
_sym_db.RegisterMessage(BalanceOnChainResponse)

_UNLOCKER = DESCRIPTOR.services_by_name['Unlocker']
_BOLTLIGHT = DESCRIPTOR.services_by_name['Boltlight']
_LIGHTNING = DESCRIPTOR.services_by_name['Lightning']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDRESS_TYPE._options = None
  _ADDRESS_TYPE._serialized_options = b'\020\001'
  _UNLOCKREQUEST._serialized_start=40
  _UNLOCKREQUEST._serialized_end=94
  _UNLOCKRESPONSE._serialized_start=96
  _UNLOCKRESPONSE._serialized_end=135
  _GETINFOREQUEST._serialized_start=137
  _GETINFOREQUEST._serialized_end=153
  _GETINFORESPONSE._serialized_start=155
  _GETINFORESPONSE._serialized_end=240
  _LOCKREQUEST._serialized_start=242
  _LOCKREQUEST._serialized_end=255
  _LOCKRESPONSE._serialized_start=257
  _LOCKRESPONSE._serialized_end=271
  _BALANCEOFFCHAINREQUEST._serialized_start=273
  _BALANCEOFFCHAINREQUEST._serialized_end=297
  _BALANCEOFFCHAINRESPONSE._serialized_start=299
  _BALANCEOFFCHAINRESPONSE._serialized_end=418
  _CHECKINVOICEREQUEST._serialized_start=420
  _CHECKINVOICEREQUEST._serialized_end=463
  _CHECKINVOICERESPONSE._serialized_start=465
  _CHECKINVOICERESPONSE._serialized_end=528
  _CLOSECHANNELREQUEST._serialized_start=530
  _CLOSECHANNELREQUEST._serialized_end=586
  _CLOSECHANNELRESPONSE._serialized_start=588
  _CLOSECHANNELRESPONSE._serialized_end=632
  _CREATEINVOICEREQUEST._serialized_start=635
  _CREATEINVOICEREQUEST._serialized_end=769
  _CREATEINVOICERESPONSE._serialized_start=771
  _CREATEINVOICERESPONSE._serialized_end=861
  _GETNODEINFOREQUEST._serialized_start=863
  _GETNODEINFOREQUEST._serialized_end=883
  _DECODEINVOICEREQUEST._serialized_start=885
  _DECODEINVOICEREQUEST._serialized_end=953
  _DECODEINVOICERESPONSE._serialized_start=956
  _DECODEINVOICERESPONSE._serialized_end=1229
  _ROUTEHINT._serialized_start=1231
  _ROUTEHINT._serialized_end=1281
  _HOPHINT._serialized_start=1284
  _HOPHINT._serialized_end=1422
  _NETWORK._serialized_start=1424
  _NETWORK._serialized_end=1493
  _NETWORK_NAME._serialized_start=1435
  _NETWORK_NAME._serialized_end=1493
  _GETNODEINFORESPONSE._serialized_start=1496
  _GETNODEINFORESPONSE._serialized_end=1654
  _LISTCHANNELSREQUEST._serialized_start=1656
  _LISTCHANNELSREQUEST._serialized_end=1698
  _LISTCHANNELSRESPONSE._serialized_start=1700
  _LISTCHANNELSRESPONSE._serialized_end=1760
  _CHANNEL._serialized_start=1763
  _CHANNEL._serialized_end=2196
  _CHANNEL_STATE._serialized_start=2097
  _CHANNEL_STATE._serialized_end=2196
  _LISTINVOICESREQUEST._serialized_start=2199
  _LISTINVOICESREQUEST._serialized_end=2428
  _LISTINVOICESRESPONSE._serialized_start=2430
  _LISTINVOICESRESPONSE._serialized_end=2490
  _ORDER._serialized_start=2492
  _ORDER._serialized_end=2543
  _ORDER_DIRECTION._serialized_start=2501
  _ORDER_DIRECTION._serialized_end=2543
  _INVOICE._serialized_start=2546
  _INVOICE._serialized_end=2908
  _INVOICE_STATE._serialized_start=2852
  _INVOICE_STATE._serialized_end=2908
  _LISTPAYMENTSREQUEST._serialized_start=2910
  _LISTPAYMENTSREQUEST._serialized_end=2931
  _LISTPAYMENTSRESPONSE._serialized_start=2933
  _LISTPAYMENTSRESPONSE._serialized_end=2993
  _PAYMENT._serialized_start=2995
  _PAYMENT._serialized_end=3110
  _LISTPEERSREQUEST._serialized_start=3112
  _LISTPEERSREQUEST._serialized_end=3130
  _LISTPEERSRESPONSE._serialized_start=3132
  _LISTPEERSRESPONSE._serialized_end=3183
  _PEER._serialized_start=3185
  _PEER._serialized_end=3254
  _LISTTRANSACTIONSREQUEST._serialized_start=3256
  _LISTTRANSACTIONSREQUEST._serialized_end=3281
  _LISTTRANSACTIONSRESPONSE._serialized_start=3283
  _LISTTRANSACTIONSRESPONSE._serialized_end=3355
  _TRANSACTION._serialized_start=3358
  _TRANSACTION._serialized_end=3506
  _NEWADDRESSREQUEST._serialized_start=3508
  _NEWADDRESSREQUEST._serialized_end=3571
  _NEWADDRESSRESPONSE._serialized_start=3573
  _NEWADDRESSRESPONSE._serialized_end=3610
  _ADDRESS._serialized_start=3612
  _ADDRESS._serialized_end=3696
  _ADDRESS_TYPE._serialized_start=3623
  _ADDRESS_TYPE._serialized_end=3696
  _OPENCHANNELREQUEST._serialized_start=3698
  _OPENCHANNELREQUEST._serialized_end=3793
  _OPENCHANNELRESPONSE._serialized_start=3795
  _OPENCHANNELRESPONSE._serialized_end=3838
  _PAYINVOICEREQUEST._serialized_start=3840
  _PAYINVOICEREQUEST._serialized_end=3953
  _PAYINVOICERESPONSE._serialized_start=3955
  _PAYINVOICERESPONSE._serialized_end=4001
  _PAYONCHAINREQUEST._serialized_start=4003
  _PAYONCHAINREQUEST._serialized_end=4081
  _PAYONCHAINRESPONSE._serialized_start=4083
  _PAYONCHAINRESPONSE._serialized_end=4117
  _UNLOCKNODEREQUEST._serialized_start=4119
  _UNLOCKNODEREQUEST._serialized_end=4156
  _UNLOCKNODERESPONSE._serialized_start=4158
  _UNLOCKNODERESPONSE._serialized_end=4178
  _BALANCEONCHAINREQUEST._serialized_start=4180
  _BALANCEONCHAINREQUEST._serialized_end=4203
  _BALANCEONCHAINRESPONSE._serialized_start=4205
  _BALANCEONCHAINRESPONSE._serialized_end=4271
  _UNLOCKER._serialized_start=4273
  _UNLOCKER._serialized_end=4346
  _BOLTLIGHT._serialized_start=4349
  _BOLTLIGHT._serialized_end=4483
  _LIGHTNING._serialized_start=4486
  _LIGHTNING._serialized_end=5868
# @@protoc_insertion_point(module_scope)
