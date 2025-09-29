#!/usr/bin/env python3

import ipaddress

def read_ip_ranges(filename):
    ranges = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    try:
                        # Handle different formats
                        if '/' in line:
                            ranges.append(ipaddress.ip_network(line, strict=False))
                        elif '-' in line:
                            # Convert range to CIDR
                            start, end = line.split('-')
                            start_ip = ipaddress.ip_address(start.strip())
                            end_ip = ipaddress.ip_address(end.strip())
                            ranges.extend(ipaddress.summarize_address_range(start_ip, end_ip))
                    except Exception as e:
                        print(f"Error processing line '{line}': {e}")
    except FileNotFoundError:
        print(f"File {filename} not found, skipping")
    return ranges

def optimize_ranges(ranges):
    if not ranges:
        return []
    # Sort ranges and merge overlapping ones
    ranges = sorted(set(ranges))
    merged = [ranges[0]]
    for current in ranges[1:]:
        last = merged[-1]
        try:
            # Check if ranges can be merged
            if (current.network_address <= last.broadcast_address + 1 and
                current.version == last.version):
                # Merge ranges
                start = min(last.network_address, current.network_address)
                end = max(last.broadcast_address, current.broadcast_address)
                merged_ranges = list(ipaddress.summarize_address_range(start, end))
                merged[-1:] = merged_ranges
            else:
                merged.append(current)
        except:
            merged.append(current)
    return merged

def main():
    # Collect all IPv4 ranges
    ipv4_ranges = []
    ipv4_ranges.extend(read_ip_ranges('maxmind-ru-ipv4.txt'))

    # Collect all IPv6 ranges
    ipv6_ranges = []
    ipv6_ranges.extend(read_ip_ranges('maxmind-ru-ipv6.txt'))

    # Merge and optimize ranges
    optimized_ipv4 = optimize_ranges(ipv4_ranges)
    optimized_ipv6 = optimize_ranges(ipv6_ranges)

    # Write final results
    with open('russian-ipv4-final.txt', 'w') as f:
        for network in optimized_ipv4:
            f.write(f"{network}\n")

    with open('russian-ipv6-final.txt', 'w') as f:
        for network in optimized_ipv6:
            f.write(f"{network}\n")

    print(f"Final result: {len(optimized_ipv4)} IPv4 ranges, {len(optimized_ipv6)} IPv6 ranges")

    # Create combined file for dat generation
    with open('russian-ip-combined.txt', 'w') as f:
        for network in optimized_ipv4:
            f.write(f"{network}\n")
        for network in optimized_ipv6:
            f.write(f"{network}\n")

    # Count total IPs
    total_ipv4 = sum(network.num_addresses for network in optimized_ipv4)
    total_ipv6 = sum(network.num_addresses for network in optimized_ipv6)

    print(f"Total IPv4 addresses: {total_ipv4:,}")
    print(f"Total IPv6 addresses: {total_ipv6:,}")

if __name__ == "__main__":
    main()