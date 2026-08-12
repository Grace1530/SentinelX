from backend.app.database.repository import repository


class PacketStore:
    def save(self, packet: dict) -> int:
        query = """
            INSERT INTO packets (
                timestamp,
                source_ip,
                destination_ip,
                source_port,
                destination_port,
                protocol,
                packet_length,
                tcp_flags,
                ttl,
                interface,
                flow_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        return repository.execute(
            query,
            [
                packet.get("timestamp"),
                packet.get("source_ip"),
                packet.get("destination_ip"),
                packet.get("source_port"),
                packet.get("destination_port"),
                packet.get("protocol"),
                packet.get("packet_length"),
                packet.get("tcp_flags"),
                packet.get("ttl"),
                packet.get("interface"),
                packet.get("flow_id"),
            ],
        )

    def save_many(self, packets: list[dict]) -> None:
        query = """
            INSERT INTO packets (
                timestamp,
                source_ip,
                destination_ip,
                source_port,
                destination_port,
                protocol,
                packet_length,
                tcp_flags,
                ttl,
                interface,
                flow_id
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = [
            (
                packet.get("timestamp"),
                packet.get("source_ip"),
                packet.get("destination_ip"),
                packet.get("source_port"),
                packet.get("destination_port"),
                packet.get("protocol"),
                packet.get("packet_length"),
                packet.get("tcp_flags"),
                packet.get("ttl"),
                packet.get("interface"),
                packet.get("flow_id"),
            )
            for packet in packets
        ]

        if values:
            repository.execute_many(query, values)


packet_store = PacketStore()