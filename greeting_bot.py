{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Greeting Bot - あいさつボット\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 🔰 あいさつボット\n",
        "# input(): ユーザーからの入力を受け取る\n",
        "# if / elif / else: 条件によって処理を分ける\n",
        "\n",
        "name = input(\"あなたの名前は？ \")\n",
        "time = input(\"今の時間帯は？（朝・昼・夜）\")\n",
        "\n",
        "if time == \"朝\":\n",
        "    print(\"おはよう、\" + name + \"さん！\")\n",
        "elif time == \"昼\":\n",
        "    print(\"こんにちは、\" + name + \"さん！\")\n",
        "elif time == \"夜\":\n",
        "    print(\"こんばんは、\" + name + \"さん！\")\n",
        "else:\n",
        "    print(\"こんにちは、\" + name + \"さん！\")\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Greeting Bot - あいさつボット",
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
