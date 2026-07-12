import boto3

# The tag we used in Terraform to name our VPC (dev-vpc)
VPC_NAME = "dev-vpc"

def main():
    # Create a client to talk to the EC2/VPC service in AWS
    ec2 = boto3.client("ec2", region_name="af-south-1")

    print(f"Checking for VPC named '{VPC_NAME}'...\n")

    # All VPCs that have a tag "Name" = "dev-vpc"
    response = ec2.describe_vpcs(
        Filters=[{"Name": "tag:Name", "Values": [VPC_NAME]}]
    )

    vpcs = response["Vpcs"]

    if not vpcs:
        print("No VPC found. Deployment may have failed or not been applied yet.")
        return

    vpc = vpcs[0]
    vpc_id = vpc["VpcId"]
    print(f"VPC found: {vpc_id}")
    print(f"CIDR block: {vpc['CidrBlock']}")
    print(f"State: {vpc['State']}\n")

    # Subnets that belong to this VPC
    subnets_response = ec2.describe_subnets(
        Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
    )

    subnets = subnets_response["Subnets"]
    print(f"Found {len(subnets)} subnet(s) in this VPC:\n")

    for subnet in subnets:
        name_tag = "No Name tag"
        for tag in subnet.get("Tags", []):
            if tag["Key"] == "Name":
                name_tag = tag["Value"]

        print(f"- {name_tag} | {subnet['CidrBlock']} | AZ: {subnet['AvailabilityZone']}")


if __name__ == "__main__":
    main()