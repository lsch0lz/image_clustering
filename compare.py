import argparse

from src.data_loader import get_images


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, help="/path/to/images/")
    parser.add_argument("--num_clusters", type=int, help="Number of Clusters")
    parser.add_argument(
        "--cluster_method", type=str, default="kmeans", help="K-Means, Cosine Similarity"
    )

    opt = parser.parse_args()
    return opt


if __name__ == "__main__":
    args = get_args()
    get_images(args.data)
