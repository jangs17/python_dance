#!/usr/bin/env python3

from scapy.all import *
import logging

# Set up logging
logging.basicConfig(filename='packet_anomalies.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Define thresholds for anomalies
MAX_PACKET_SIZE = 1500  # Typical MTU size for Ethernet
MIN_PACKET_SIZE = 64    # Typical minimum packet size
LOW_TTL_THRESHOLD = 10  # Unusually low TTL value

def packet_callback(packet):
    try:
        # Get packet size
        packet_size = len(packet)
        packet_info = {
            'size': packet_size,
            'src': packet[IP].src if IP in packet else 'N/A',
            'dst': packet[IP].dst if IP in packet else 'N/A',
            'protocol': packet[IP].proto if IP in packet else 'N/A',
            'ttl': packet[IP].ttl if IP in packet else 'N/A'
        }
        
        # Check for size anomalies
        if packet_size > MAX_PACKET_SIZE:
            logging.info(f"Large packet detected: {packet_info}")
        elif packet_size < MIN_PACKET_SIZE:
            logging.info(f"Small packet detected: {packet_info}")

        # Check for unusual header values
        if IP in packet:
            ip_packet = packet[IP]
            if ip_packet.ttl < LOW_TTL_THRESHOLD:
                logging.info(f"Low TTL detected: {packet_info}")
            if ip_packet.flags & 2:  # Check for the 'DF' (Don't Fragment) flag
                logging.info(f"Don't Fragment flag set: {packet_info}")

        # Add other checks and useful details for the security researcher
        if TCP in packet:
            tcp_packet = packet[TCP]
            packet_info.update({
                'src_port': tcp_packet.sport,
                'dst_port': tcp_packet.dport,
                'flags': tcp_packet.flags
            })
            if tcp_packet.flags == 0:
                logging.info(f"TCP packet with no flags set: {packet_info}")

        if UDP in packet:
            udp_packet = packet[UDP]
            packet_info.update({
                'src_port': udp_packet.sport,
                'dst_port': udp_packet.dport,
                'length': udp_packet.len
            })
            if udp_packet.len == 0:
                logging.info(f"UDP packet with zero length: {packet_info}")

    except Exception as e:
        logging.error(f"Error processing packet: {e}")

def main():
    print("Starting packet capture. Press Ctrl+C to stop.")
    # Start sniffing packets
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()


