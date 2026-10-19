
import { useEffect, useState } from "react";
import axios from "axios";

interface Order {
  id: number;
  product_name: string;
  amount: string;
  status: "pending" | "dispatche" | "delivered" | "cancelled";
  carrier: string;
  tracking_number: string;
  delivery_address: string;
  created_at: string | null;
}

export default function OrdersList() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await axios.get<Order[]>(
          "http://localhost:8000/api/orders/"
        );

        setOrders(response.data);
      } catch (err) {
        if (axios.isAxiosError(err)) {
          setError(
            err.response?.data?.detail ||
              "Failed to fetch orders."
          );
        } else {
          setError("An unexpected error occurred.");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchOrders();
  }, []);

  if (loading) {
    return <p className="p-6">Loading orders...</p>;
  }

  if (error) {
    return <p className="p-6 text-red-500">{error}</p>;
  }

  return (
    <div className="p-6">
      <h1 className="mb-6 text-2xl font-bold">My Orders</h1>

      {orders.length === 0 ? (
        <p>You have no orders yet.</p>
      ) : (
        <div className="space-y-4">
          {orders.map((order) => (
            <div
              key={order.id}
              className="rounded-lg border p-4 shadow-sm"
            >
              <div className="flex items-center justify-between gap-4">
                <h2 className="text-lg font-semibold">
                  Order #{order.id}
                </h2>

                <span className="rounded-full bg-gray-100 px-3 py-1 text-sm">
                  {order.status}
                </span>
              </div>

              <div className="mt-3 space-y-2">
                <p>
                  <strong>Product:</strong> {order.product_name}
                </p>

                <p>
                  <strong>Amount:</strong> {order.amount}
                </p>

                <p>
                  <strong>Carrier:</strong>{" "}
                  {order.carrier || "Not assigned"}
                </p>

                <p>
                  <strong>Tracking number:</strong>{" "}
                  {order.tracking_number || "Not available"}
                </p>

                <p>
                  <strong>Delivery address:</strong>{" "}
                  {order.delivery_address || "Not provided"}
                </p>

                <p>
                  <strong>Created at:</strong>{" "}
                  {order.created_at
                    ? new Date(order.created_at).toLocaleString()
                    : "Not available"}
                </p>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
