from collections import defaultdict, deque
import functools
import math
import re

class Packet(object):
    def __init__(self, version, type):
        self.version = version
        self.type = type
        self.literal = None
        self.sub_packets = []


def part1(data):
    binary = bin(int(data, 16))[2:]
    while len(binary) % 4 != 0:
        binary = '0' + binary

    packet, _ = parse_packet(curr_bit=0, binary=binary)
    q = deque([packet])
    sum_versions = 0
    while q:
        packet = q.popleft()
        sum_versions += packet.version
        for sub_p in packet.sub_packets:
            q.append(sub_p)
    return sum_versions


def parse_packet(curr_bit, binary):
    version = int(binary[curr_bit:curr_bit + 3], 2)
    type = int(binary[curr_bit + 3:curr_bit + 6], 2)
    curr_bit += 6
    packet = Packet(version, type)

    if packet.type == 4:
        curr_bit = parse_literal(packet, curr_bit, binary)
    else:
        length_type = binary[curr_bit]
        curr_bit += 1
        if length_type == '1':
            num_subpackets = parse_bits(11, curr_bit, binary)
            curr_bit += 11
            for _ in range(num_subpackets):
                sub_packet, curr_bit = parse_packet(curr_bit, binary)
                packet.sub_packets.append(sub_packet)
        else:
            length_subpackets = parse_bits(15, curr_bit, binary)
            curr_bit += 15
            end_bit = curr_bit + length_subpackets
            while curr_bit < end_bit:
                sub_packet, curr_bit = parse_packet(curr_bit, binary)
                packet.sub_packets.append(sub_packet)
    return packet, curr_bit


def parse_literal(packet, curr_bit, binary):
    bin_num = ''
    while True:
        if binary[curr_bit] == '1':
            b = False
        else:
            b = True

        bin_num += binary[curr_bit + 1:curr_bit + 5]
        curr_bit += 5

        if b:
            packet.literal = int(bin_num, 2)
            return curr_bit


def parse_bits(num_bits, curr_bit, binary):
    return int(binary[curr_bit:curr_bit + num_bits], 2)


def part2(data):
    binary = bin(int(data, 16))[2:]
    while len(binary) % 4 != 0:
        binary = '0' + binary

    packet, _ = parse_packet(curr_bit=0, binary=binary)

    return evaluate_packet(packet)


def evaluate_packet(packet):
    if packet.literal:
        return packet.literal

    packet_evaluations = [evaluate_packet(p) for p in packet.sub_packets]

    if packet.type == 0:
        return sum(packet_evaluations)

    if packet.type == 1:
        product = 1
        for v in packet_evaluations:
            product *= v
        return product

    if packet.type == 2:
        return min(packet_evaluations)

    if packet.type == 3:
        return max(packet_evaluations)

    if packet.type == 5:
        if packet_evaluations[0] > packet_evaluations[1]:
            return 1
        return 0

    if packet.type == 6:
        if packet_evaluations[0] < packet_evaluations[1]:
            return 1
        return 0

    if packet.type == 7:
        if packet_evaluations[0] == packet_evaluations[1]:
            return 1
        return 0
