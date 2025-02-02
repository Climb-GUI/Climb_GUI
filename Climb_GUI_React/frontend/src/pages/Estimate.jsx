import React, { useState } from "react";
import NavBar from "../components/NavBar";
import axios from "axios";
import "../index.css";

function Estimate() {
	const [selectedFile, setSelectedFile] = useState(null);
	const [originalImageUrl, setOriginalImageUrl] = useState("");
	const [alteredImageUrl, setAlteredImageUrl] = useState("");
	const [loading, setLoading] = useState(false);
	const [allColors, setAllColors] = useState({
		red: false,
		green: false,
		blue: false,
		orange: false,
		purple: false,
		yellow: false,
		black: false,
	});

	const handleFileChange = (event) => {
		const file = event.target.files[0];
		if (file) {
			setSelectedFile(file);
			setOriginalImageUrl(URL.createObjectURL(file));
			setAlteredImageUrl(null);

			event.target.value = null;
		}
	};

	const handleSubmit = async (event) => {
		event.preventDefault();
		if (!selectedFile) return;

		setLoading(true);

		const formData = new FormData();
		formData.append("file", selectedFile);

		try {
			const cols = [];

			Object.entries(allColors).forEach(([color, isSelected]) => {
				if (isSelected) {
					cols.push(color);
				}
			});

			const param = cols.length > 0 ? cols.join(",") : "all";

			const response = await axios.post(
				`${import.meta.env.VITE_BACKEND_URL}/api/getPath/${param}`,
				formData,
				{
					headers: {
						"Content-Type": "multipart/form-data",
						Authorization: `Bearer ${import.meta.env.VITE_API_KEY}`,
					},
					responseType: "blob",
				},
			);

			// Create a URL for the altered image blob
			const imageBlob = new Blob([response.data], { type: "image/png" });
			const imageUrl = URL.createObjectURL(imageBlob);
			setAlteredImageUrl(imageUrl);
			setOriginalImageUrl(null);

			setLoading(false);
		} catch (error) {
			setLoading(false);
			window.alert("Some error occurred");
			console.error("Error uploading file:", error);
		}
	};

	const handleClearImage = () => {
		setSelectedFile(null);
		setOriginalImageUrl("");
		setAlteredImageUrl("");
	};

	const handleClearColors = () => {
		setAllColors({
			red: false,
			green: false,
			blue: false,
			orange: false,
			purple: false,
			yellow: false,
			black: false,
		});
	};

	return (
		<>
			{loading && <Spinner />}
			<NavBar />
			<div className="container mx-auto px-4 py-8 text-center">
				<h1 className="text-3xl font-bold mb-6 text-gray-800">
					Bouldering Best Path Estimator
				</h1>

				<p>
					Note: This is being run all on free servers, so expect to wait up to a
					minute for the analysis to complete.
				</p>

				<div className="bg-white shadow-lg rounded-lg p-6 mb-8">
					<h2 className="text-xl font-semibold mb-4 text-gray-700">
						Upload Your Bouldering Image
					</h2>
					<form onSubmit={handleSubmit} className="flex flex-col items-center">
						<input
							type="file"
							accept="image/*"
							onChange={handleFileChange}
							className="hidden"
							id="file-upload"
						/>
						<label
							htmlFor="file-upload"
							className="cursor-pointer bg-blue-500 text-white px-4 py-2 rounded-lg shadow hover:bg-blue-600 transition"
						>
							Choose Image
						</label>
						<div className="mt-4 space-x-4">
							<button
								type="submit"
								className="bg-green-500 text-white px-6 py-2 rounded-lg shadow hover:bg-green-600 transition"
							>
								Upload and Analyze
							</button>
							<button
								type="button"
								onClick={handleClearImage}
								className="bg-red-500 text-white px-6 py-2 rounded-lg shadow hover:bg-red-600 transition"
							>
								Clear Image
							</button>
						</div>
					</form>
				</div>

				<div className="bg-white shadow-lg rounded-lg p-6 mb-8">
					<h2 className="text-xl font-semibold mb-4 text-gray-700">
						Select Path Colors
					</h2>
					<p className="text-gray-600 mb-4">
						Choose specific colors to estimate the best path. If none are
						selected, all colors will be analyzed.
					</p>
					<div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-4">
						{Object.keys(allColors).map((color) => (
							<div key={color} className="flex items-center space-x-2">
								<input
									type="checkbox"
									id={color}
									checked={allColors[color]}
									onChange={() =>
										setAllColors((prev) => ({
											...prev,
											[color]: !allColors[color],
										}))
									}
									className="h-4 w-4 text-blue-500 focus:ring focus:ring-blue-200 rounded"
								/>
								<label htmlFor={color} className="text-gray-700 capitalize">
									{color}
								</label>
							</div>
						))}
					</div>
					<button
						type="button"
						onClick={handleClearColors}
						className="bg-yellow-500 text-white px-4 py-2 rounded-lg shadow hover:bg-yellow-600 transition"
					>
						Clear Colors
					</button>
				</div>

				<div className="bg-white shadow-lg rounded-lg p-6">
					{originalImageUrl && (
						<div>
							<h2 className="text-xl font-semibold mb-4 text-gray-700">
								Original Image
							</h2>
							<img
								src={originalImageUrl}
								alt="Original"
								className="rounded-lg border border-gray-300 w-96 h-auto mx-auto"
							/>
						</div>
					)}

					{alteredImageUrl && (
						<div>
							<h2 className="text-xl font-semibold mb-4 text-gray-700">
								Best Path Visualization
							</h2>
							<img
								src={alteredImageUrl}
								alt="Altered Best Path"
								className="rounded-lg border border-gray-300 w-96 h-auto mx-auto"
							/>
						</div>
					)}
				</div>
			</div>
		</>
	);
}

const Spinner = () => {
	return (
		<div className="fixed inset-0 flex items-center justify-center backdrop-blur-[2px] bg-black/10">
			<div className="flex items-end space-x-1 h-12">
				{[...Array(5)].map((_, i) => (
					<div
						key={i}
						className="w-2 bg-blue-500 rounded-full animate-[bounce_1s_ease-in-out_infinite]"
						style={{
							height: "60%",
							animationDelay: `${i * 0.15}s`,
						}}
					>
						<div className="w-full h-full bg-gradient-to-t from-blue-600 to-blue-400 rounded-full opacity-80" />
					</div>
				))}
			</div>

			{/* Subtle reflection */}
			<div className="absolute mt-14 flex items-start space-x-1 h-12 opacity-20 scale-y-[-0.4] blur-sm">
				{[...Array(5)].map((_, i) => (
					<div
						key={i}
						className="w-2 bg-blue-500 rounded-full animate-[bounce_1s_ease-in-out_infinite]"
						style={{
							height: "60%",
							animationDelay: `${i * 0.15}s`,
						}}
					>
						<div className="w-full h-full bg-gradient-to-t from-blue-600 to-blue-400 rounded-full" />
					</div>
				))}
			</div>
		</div>
	);
};

export default Estimate;
